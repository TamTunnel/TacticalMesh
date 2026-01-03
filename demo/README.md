# TacticalMesh Demo

This directory contains automated scripts to demonstrate the capabilities of TacticalMesh.

## Contents

- `start.sh`: Launches the full stack (via Docker Compose) and starts the scenario simulation.
- `stop.sh`: Stops the Docker containers.
- `scenario.py`: Python script that simulates:
    - 4 Nodes (Vehicle, Dismounted, UAS, Sensor)
    - Registration of nodes
    - Periodic heartbeats with moving GPS coordinates
    - Telemetry (CPU, Battery, etc.)

## Quick Start

1. **Run the demo:**

    ```bash
    ./start.sh
    ```

2. **Access the Dashboard:**
    - Open [http://localhost:3000](http://localhost:3000)
    - Login with:
        - Username: `admin`
        - Password: `admin123`

3. **Observe:**
    - Go to the **Nodes** tab to see the live nodes.
    - Watch the "Last Seen" and telemetry update in real-time.

4. **Stop:**
    - Press `Ctrl+C` to stop the simulation script.
    - Run `./stop.sh` to stop the containers.
