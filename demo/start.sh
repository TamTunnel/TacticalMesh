#!/bin/bash
set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== TacticalMesh Demo Launcher ===${NC}"

# Check for Docker
if ! command -v docker &> /dev/null; then
    echo "Error: Docker is required but not found."
    exit 1
fi

echo -e "${GREEN}1. Starting Infrastructure (Docker Compose)...${NC}"
docker-compose up -d --build

echo -e "${GREEN}2. Setting up Demo Environment...${NC}"
# Setup Python venv for demo if needed, or just install requirements
if [ ! -d "demo/venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv demo/venv
fi

source demo/venv/bin/activate
pip install -r demo/requirements.txt > /dev/null

echo -e "${GREEN}3. Running Scenario...${NC}"
echo "Dashboard available at: http://localhost:3000"
echo "Login: admin / admin123"
echo "Press Ctrl+C to stop the scenario (containers will keep running)."
echo ""

python3 demo/scenario.py
