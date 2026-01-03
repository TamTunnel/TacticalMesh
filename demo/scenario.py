#!/usr/bin/env python3
"""
TacticalMesh Demo Scenario
Simulates a live tactical environment with moving nodes and traffic.
"""
import sys
import time
import random
import requests
import signal
import logging
from datetime import datetime
from rich.console import Console
from rich.logging import RichHandler
from rich.progress import Progress, SpinnerColumn, TextColumn

# Configure logging
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True, markup=True)]
)
log = logging.getLogger("demo")
console = Console()

API_URL = "http://localhost:8000/api/v1"

# Scenario Configuration
NODES = [
    {
        "node_id": "alpha-1",
        "name": "Alpha One",
        "node_type": "vehicle",
        "description": "Command Vehicle",
        "lat": 34.0522,
        "lon": -118.2437
    },
    {
        "node_id": "bravo-team",
        "name": "Bravo Team",
        "node_type": "dismounted",
        "description": "Infantry Squad",
        "lat": 34.0530, 
        "lon": -118.2440
    },
    {
        "node_id": "uav-recon",
        "name": "Eagle Eye",
        "node_type": "uas",
        "description": "Recon Drone",
        "lat": 34.0540,
        "lon": -118.2450
    },
    {
        "node_id": "sensor-grid-1",
        "name": "Sensor 1",
        "node_type": "sensor",
        "description": "Perimeter Sensor",
        "lat": 34.0510,
        "lon": -118.2420
    }
]

class DemoScenario:
    def __init__(self):
        self.node_tokens = {}
        self.running = True
        
    def wait_for_api(self):
        """Wait for the API to become available."""
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            task = progress.add_task(description="Waiting for API...", total=None)
            while self.running:
                try:
                    resp = requests.get(f"{API_URL}/health", timeout=5)
                    if resp.status_code == 200:
                        log.info("[green]API is online![/green]")
                        return
                except requests.exceptions.RequestException:
                    pass
                time.sleep(2)

    def register_nodes(self):
        """Register all scenario nodes."""
        log.info("Registering nodes...")
        for node_data in NODES:
            try:
                # Extract meta fields not for registration
                reg_data = {
                    "node_id": node_data["node_id"],
                    "name": node_data["name"],
                    "node_type": node_data["node_type"],
                    "description": node_data["description"],
                    "ip_address": f"192.168.1.{len(self.node_tokens) + 10}",
                    "mac_address": f"00:11:22:33:44:{len(self.node_tokens) + 10:02x}"
                }
                
                resp = requests.post(f"{API_URL}/nodes/register", json=reg_data)
                resp.raise_for_status()
                data = resp.json()
                self.node_tokens[node_data["node_id"]] = data["auth_token"]
                log.info(f"Registered [bold cyan]{node_data['name']}[/bold cyan] ({node_data['node_id']})")
            except Exception as e:
                log.error(f"Failed to register {node_data['node_id']}: {e}")

    def simulate_heartbeats(self):
        """Send heartbeats for all nodes with simulated movement."""
        log.info("Simulating network traffic... (Press Ctrl+C to stop)")
        
        while self.running:
            for node in NODES:
                try:
                    # Simulate movement (random walk)
                    node["lat"] += random.uniform(-0.0001, 0.0001)
                    node["lon"] += random.uniform(-0.0001, 0.0001)
                    
                    # Simulate varying stats
                    cpu = random.randint(10, 80)
                    if node["node_type"] == "uas":
                        altitude = 300 + random.randint(-10, 10)
                    else:
                        altitude = 0
                        
                    heartbeat_data = {
                        "node_id": node["node_id"],
                        "cpu_usage": cpu,
                        "memory_usage": random.randint(20, 60),
                        "disk_usage": 45,
                        "latitude": node["lat"],
                        "longitude": node["lon"],
                        "altitude": altitude,
                        "custom_metrics": {"battery": random.randint(80, 100)}
                    }
                    
                    token = self.node_tokens.get(node["node_id"])
                    headers = {"Authorization": f"Bearer {token}"} if token else {}
                    
                    resp = requests.post(
                        f"{API_URL}/nodes/heartbeat", 
                        json=heartbeat_data,
                        headers=headers
                    )
                    
                    if resp.status_code != 200:
                        log.warning(f"Heartbeat failed for {node['node_id']}: {resp.status_code}")
                        
                except Exception as e:
                    log.error(f"Error in simulation loop: {e}")
            
            time.sleep(2)

    def stop(self, signum, frame):
        self.running = False
        print("\nStopping simulation...")
        sys.exit(0)

if __name__ == "__main__":
    scenario = DemoScenario()
    signal.signal(signal.SIGINT, scenario.stop)
    
    console.print("[bold green]TacticalMesh Demo Scenario[/bold green]")
    scenario.wait_for_api()
    scenario.register_nodes()
    scenario.simulate_heartbeats()
