# TacticalMesh Live Demo Guide

This guide explains how to run the automated demo scenario for TacticalMesh. This demo is designed to showcase the platform's capabilities to stakeholders by simulating a live tactical environment.

## Prerequisites

- **Docker** and **Docker Compose** installed.
- **Python 3.8+** (for the simulation script).

## Scenario Overview

The demo simulates a "Bravo Company" operation with the following assets:

1.  **Alpha One (Vehicle)**: A command vehicle moving south.
2.  **Bravo Team (Dismounted)**: An infantry squad moving alongside.
3.  **Eagle Eye (UAS)**: An unmanned aerial system providing aerial coverage (loitering).
4.  **Sensor 1 (Fixed)**: A perimeter sensor.

The simulation generates:

- **Registration traffic**: Nodes joining the mesh.
- **Heartbeats**: Periodic status updates with:
    - GPS Coordinates (Latitude/Longitude/Altitude)
    - Resource usage (CPU, Memory)
    - Battery levels

## Running the Demo

### Option 1: Web Console (Recommended)

1.  Start the application stack:
    ```bash
    docker-compose up -d
    ```
2.  Open [http://localhost:3000](http://localhost:3000) and login as `admin`.
3.  Navigate to **Settings**.
4.  Toggle **Demo Mode** to **RUNNING**.
5.  Go to the **Nodes** tab to watch the action.

### Option 2: CLI Script

Navigate to the project root and execute:
`bash
    ./demo/start.sh
    `
This script will: - Start the backend, frontend, database, and redis containers. - Create a local Python virtual environment. - Install necessary dependencies (`requests`, `rich`). - Wait for the API to become healthy. - Launch the `scenario.py` simulation.

## What to Show

Once the demo is running, log in to the **Web Console** at [http://localhost:3000](http://localhost:3000) (`admin` / `admin123`).

### 1. Dashboard (Network Overview)

- Show the **Active Nodes** count (should be 4).
- Explain the **Network Health** metrics.

### 2. Nodes View

- Navigate to the **Nodes** page.
- Highlight the **Real-time updates**: "Last Seen" timestamps refreshing every few seconds.
- Show the **Node Types** icons (Vehicle, Soldier, Drone).
- Click on **Eagle Eye** to show specific metadata (Altitude, etc.).

## Troubleshooting

- **Containers fail to start**: Ensure ports 3000 (frontend) and 8000 (backend) are free.
- **Simulation crashes**: Check permissions for `demo/start.sh` and ensure Python 3 is available.
- **No data in dashboard**: Ensure you are logged in and the simulation script is printing "Heartbeat sent" logs.
