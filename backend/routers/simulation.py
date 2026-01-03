# Copyright 2024 TacticalMesh Contributors
# SPDX-License-Identifier: Apache-2.0
"""
Simulation router.

Provides endpoints to control the live demo simulation.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

from ..auth import require_admin
from ..models import User
from ..simulation import simulation_manager

router = APIRouter(prefix="/api/v1/simulation", tags=["Simulation"])

class SimulationStatus(BaseModel):
    active: bool
    nodes_count: int
    simulated_nodes: int
    start_time: str = None

@router.get("/status", response_model=SimulationStatus)
async def get_simulation_status(
    current_user: User = Depends(require_admin)
):
    """Get current simulation status."""
    status = simulation_manager.status
    return SimulationStatus(
        active=status["active"],
        nodes_count=status["nodes_count"],
        simulated_nodes=status["simulated_nodes"],
        start_time=str(status["start_time"]) if status["start_time"] else None
    )

@router.post("/start", status_code=status.HTTP_202_ACCEPTED)
async def start_simulation(
    current_user: User = Depends(require_admin)
):
    """Start the live demo simulation."""
    if simulation_manager.is_running:
        return {"message": "Simulation already running"}
    
    await simulation_manager.start()
    return {"message": "Simulation started"}

@router.post("/stop", status_code=status.HTTP_202_ACCEPTED)
async def stop_simulation(
    current_user: User = Depends(require_admin)
):
    """Stop the live demo simulation."""
    if not simulation_manager.is_running:
        return {"message": "Simulation not running"}
    
    await simulation_manager.stop()
    return {"message": "Simulation stopped"}
