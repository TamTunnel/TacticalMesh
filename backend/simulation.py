# Copyright 2024 TacticalMesh Contributors
# SPDX-License-Identifier: Apache-2.0
"""
Simulation Engine for TacticalMesh.

This module provides the core logic for the integrated demo mode,
simulating node movement and heartbeats using internal API calls.
"""

import asyncio
import logging
import random
from datetime import datetime
from typing import Dict, List, Optional
import httpx

from .config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()

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

class SimulationManager:
    """Manages the lifecycle of the demo simulation."""
    
    def __init__(self):
        self._running = False
        self._task: Optional[asyncio.Task] = None
        self._node_tokens: Dict[str, str] = {}
        self._start_time: Optional[datetime] = None
        
    @property
    def is_running(self) -> bool:
        return self._running
        
    @property
    def status(self) -> dict:
        return {
            "active": self._running,
            "nodes_count": len(self._node_tokens),
            "simulated_nodes": len(NODES),
            "start_time": self._start_time
        }

    async def start(self):
        """Start the simulation if not already running."""
        if self._running:
            return
            
        logger.info("Starting simulation engine...")
        self._running = True
        self._start_time = datetime.utcnow()
        self._task = asyncio.create_task(self._simulation_loop())

    async def stop(self):
        """Stop the simulation."""
        if not self._running:
            return
            
        logger.info("Stopping simulation engine...")
        self._running = False
        if self._task:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
            self._task = None
        self._node_tokens.clear()
        self._start_time = None

    async def _simulation_loop(self):
        """Main simulation loop."""
        base_url = f"http://localhost:{settings.port}/api/v1"
        
        async with httpx.AsyncClient(timeout=10.0) as client:
            # 1. Register Nodes
            await self._register_nodes(client, base_url)
            
            # 2. Heartbeat Loop
            while self._running:
                try:
                    await self._send_heartbeats(client, base_url)
                    await asyncio.sleep(2.0)
                except asyncio.CancelledError:
                    raise
                except Exception as e:
                    logger.error(f"Simulation loop error: {e}")
                    await asyncio.sleep(5.0)  # Backoff on error

    async def _register_nodes(self, client: httpx.AsyncClient, base_url: str):
        """Register all simulated nodes."""
        for i, node_data in enumerate(NODES):
            if not self._running:
                break
                
            try:
                reg_data = {
                    "node_id": node_data["node_id"],
                    "name": node_data["name"],
                    "node_type": node_data["node_type"],
                    "description": node_data["description"],
                    "ip_address": f"192.168.1.{i + 10}",
                    "mac_address": f"00:11:22:33:44:{i + 10:02x}",
                    "node_metadata": {"simulated": True}
                }
                
                # Admin token/auth is not needed for registration endpoint based on current implementation
                # but let's check if we need headers.
                # Looking at nodes.py via memory: register_node does NOT require auth.
                
                response = await client.post(f"{base_url}/nodes/register", json=reg_data)
                response.raise_for_status()
                
                data = response.json()
                self._node_tokens[node_data["node_id"]] = data["auth_token"]
                logger.info(f"Simulated node registered: {node_data['node_id']}")
                
            except Exception as e:
                logger.error(f"Failed to register simulated node {node_data['node_id']}: {e}")

    async def _send_heartbeats(self, client: httpx.AsyncClient, base_url: str):
        """Send heartbeats for all registered nodes with movement."""
        for node in NODES:
            if not self._running:
                break
                
            token = self._node_tokens.get(node["node_id"])
            if not token:
                continue

            try:
                # Update position (Random Walk)
                node["lat"] += random.uniform(-0.0001, 0.0001)
                node["lon"] += random.uniform(-0.0001, 0.0001)
                
                # Update stats
                cpu = random.randint(10, 80)
                altitude = 300 + random.randint(-10, 10) if node["node_type"] == "uas" else 0
                
                heartbeat_data = {
                    "node_id": node["node_id"],
                    "cpu_usage": cpu,
                    "memory_usage": random.randint(20, 60),
                    "disk_usage": 45,
                    "latitude": node["lat"],
                    "longitude": node["lon"],
                    "altitude": altitude,
                    "custom_metrics": {"battery": random.randint(80, 100), "signal": random.randint(-90, -50)}
                }
                
                headers = {"Authorization": f"Bearer {token}"}
                await client.post(
                    f"{base_url}/nodes/heartbeat",
                    json=heartbeat_data,
                    headers=headers
                )
                
            except Exception as e:
                pass  # Ignore transient errors

# Global instance
simulation_manager = SimulationManager()
