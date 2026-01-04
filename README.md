# TacticalMesh

**Open-Source Tactical Edge Networking Platform**

[![CI](https://github.com/TamTunnel/TacticalMesh/actions/workflows/ci.yml/badge.svg)](https://github.com/TamTunnel/TacticalMesh/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![OpenAPI](https://img.shields.io/badge/OpenAPI-3.0-green.svg)](https://swagger.io/specification/)

---

## One-Line Summary

TacticalMesh is an open-source, decentralized mesh networking platform that enables resilient command-and-control communications between edge nodes in contested or infrastructure-denied environments.

### The Simple Explanation (Analogy)

Think of it like **Waze for military radios**:

- **Waze** finds the fastest driving route by checking traffic.
- **TacticalMesh** finds the fastest communication path by checking which soldiers can reach headquarters.

If one road is blocked (radio is jammed), Waze finds another route. Same with TacticalMesh—if one path fails, it automatically finds another soldier to relay through.

---

## Problem Statement

### The Operational Reality

Modern defense operations, disaster response scenarios, and civil resilience efforts face a common challenge: **communications in contested environments**.

Consider these operational realities:

- **Contested Spectrum:** Adversary jamming and interference degrade traditional radio links
- **Destroyed Infrastructure:** After natural disasters or in conflict zones, cell towers and network infrastructure may be non-functional
- **Mobility Requirements:** Vehicles, dismounted units, sensors, and UAS must maintain connectivity while moving
- **Coalition Operations:** Allied forces must interoperate, often with incompatible proprietary systems
- **Disconnected Operations:** Forward units may be cut off from headquarters for extended periods

### Why Current Systems Fall Short

Existing tactical networking solutions suffer from critical limitations:

| Challenge             | Impact                                                                                                     |
| --------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Vendor Lock-in**    | Proprietary systems create single-vendor dependencies with long procurement cycles and limited flexibility |
| **Cost**              | Military-grade mesh radios cost $10,000–$50,000+ per unit, limiting widespread deployment                  |
| **Interoperability**  | Different systems cannot communicate, hindering coalition operations                                       |
| **Adaptability**      | Closed systems cannot be rapidly modified to address emerging threats                                      |
| **Supply Chain Risk** | Proprietary hardware creates supply chain vulnerabilities                                                  |

---

## Competitor and Landscape Analysis

### Categories of Existing Solutions

#### 1. Proprietary Military Mesh Systems

Traditional defense contractors offer specialized tactical radio systems with integrated mesh networking:

- **Strengths:** Proven in military environments, designed for specific frequency bands
- **Weaknesses:** Extremely high cost, vendor lock-in, slow innovation cycles, limited customization

#### 2. Commercial Mesh Networking

Commercial mesh solutions designed for IoT and enterprise applications:

- **Strengths:** Lower cost, widely available
- **Weaknesses:** Not designed for contested environments, lack tactical features, no disconnected operation support

#### 3. Open RAN Initiatives

Telecom-focused efforts to open radio access network interfaces:

- **Strengths:** Open standards, multi-vendor support
- **Weaknesses:** Infrastructure-centric, not designed for tactical edge, assumes reliable backhaul

### The Gaps TacticalMesh Addresses

| Gap                      | TacticalMesh Approach                                |
| ------------------------ | ---------------------------------------------------- |
| Vendor Lock-in           | Fully open-source with Apache 2.0 license            |
| High Cost                | Runs on commodity hardware (Raspberry Pi, x86 boxes) |
| Closed Code              | Transparent, auditable source code                   |
| Slow Innovation          | Community-driven development with rapid iteration    |
| Interoperability         | OpenAPI-first design for easy integration            |
| Single Points of Failure | Decentralized architecture with graceful degradation |

---

## What TacticalMesh Provides

### Core Benefits

✅ **Resilient Edge Networking** — Nodes continue operating when disconnected from the central controller, with automatic reconnection and state synchronization

✅ **Open-Source Transparency** — Full source code visibility enables security audits, customization, and elimination of supply chain black boxes

✅ **Commodity Hardware** — Deploy on Raspberry Pi, NVIDIA Jetson, commercial edge servers, or any Linux platform

✅ **OpenAPI Integration** — Standard REST APIs enable integration with existing C2 systems, sensor networks, and enterprise applications

✅ **Role-Based Access Control** — Granular permissions for administrators, operators, and observers with complete audit logging

✅ **Dual-Use Design** — Applicable to defense, disaster response, remote industrial operations, and civil resilience

### Target Deployment Scenarios

- **Military Edge Networks:** Connecting vehicles, dismounted units, sensors, and small UAS in tactical environments
- **Disaster Response:** Rapidly deployable communications for first responders when infrastructure is destroyed
- **Remote Operations:** Industrial sites, research stations, and maritime vessels with intermittent connectivity
- **Coalition Operations:** Interoperable command and control for allied forces with different native systems

### Representative Use Cases

**1. Platoon‑Level Edge Network in Contested Spectrum** -
In a high‑threat environment, a platoon operating beyond the range of fixed infrastructure needs resilient local communications between vehicles, dismounted soldiers, and unattended sensors. TacticalMesh is deployed on small edge computers (e.g., ruggedized Raspberry Pi‑class devices) mounted in vehicles and carried in rucksacks. Each node runs the agent, registering with a nearby controller when available and continuing to exchange health and status information when disconnected. Operators use the web console to see which squads and sensors are online, issue simple commands (e.g., reconfigure reporting intervals, enable/disable a sensor), and review audit logs showing who changed what and when. This enables commanders to maintain situational awareness even when satellite and cellular links are degraded or denied.

**2. Coalition / Joint Exercise Lab Environment** -
During a joint or coalition training exercise, multiple nations want to experiment with different radio stacks, edge devices, and command‑and‑control systems without locking into a single vendor. TacticalMesh is deployed in a lab environment as the common “control‑plane” fabric: each participating nation connects its own radios and edge nodes via the TacticalMesh agent and integrates its national C2 prototypes via the OpenAPI interface. The open, Apache‑licensed controller provides shared visibility of node status and command delivery while allowing each partner to keep its own radio hardware and national applications. This supports experimentation with coalition interoperability while maintaining clean separation of sensitive national capabilities.

**3. Rapid Response / Disaster Relief Network (Dual‑Use)** -
After a major natural disaster, civil authorities and military support units need to stand up a local communications fabric quickly in an area with damaged infrastructure. TacticalMesh is deployed on commercial off‑the‑shelf edge devices placed at command posts, field hospitals, and logistics hubs. The agent software forms a local control‑plane mesh, reporting basic health and location information back to a central controller when power and connectivity are available. The operations console gives incident commanders a single view of which sites are reachable, which edge nodes are overloaded, and where to direct scarce resources. This dual‑use scenario allows organizations to evaluate the platform in peacetime humanitarian missions while using the same codebase that can later be hardened for military operations.

**4. Vendor‑Neutral Integration Testbed** -
A defense program office or integrator wants to test multiple radios, routers, and edge compute platforms from different vendors without relying on any one vendor’s proprietary management stack. TacticalMesh is used as a neutral integration layer: each device hosts a small agent that normalizes status and telemetry into a common schema. The program office connects their existing monitoring tools and prototypes to the controller’s OpenAPI endpoints to evaluate performance, resilience, and behavior under fault conditions. Because TacticalMesh is Apache‑licensed and open, the testbed can be shared with contractors, FFRDCs, and allied labs without complex licensing agreements, while still leaving final export‑control decisions to each organization.

---

## 🚀 Live Demo

**New!** You can now run the demo directly from the Web Console:

1. Log in (`admin` / `admin123`).
2. Go to **Settings**.
3. Toggle **Demo Mode** to start the simulation.

Alternatively, you can run the CLI simulation script:

```bash
./demo/start.sh
```

This spins up the full stack and simulates a tactical network with vehicles, drones, and soldiers moving in real-time. See the [Demo Guide](docs/DEMO.md) for more details.

## Key Features (v0.1)

### Node Management

- **Registration & Discovery:** Automatic node registration with the central controller
- **Heartbeat Monitoring:** Real-time health status with configurable intervals
- **Telemetry Collection:** CPU, memory, disk usage, and GPS location (when available)
- **Graceful Degradation:** Nodes operate independently when disconnected

### Command & Control

- **Command Dispatch:** Send commands to individual nodes or groups
- **Command Types:** Ping, configuration updates, role changes, and custom actions
- **Status Tracking:** Full lifecycle tracking from pending to completion
- **Audit Trail:** Complete logging of all operator actions

### Security & Access Control

- **JWT Authentication:** Standard token-based authentication
- **Role-Based Permissions:**
    - **Admin:** Full system access including user management
    - **Operator:** Node and command management
    - **Observer:** Read-only access to status and history
- **Rate Limiting:** 5 login attempts per minute, 10 registrations per minute
- **Account Lockout:** 15-minute lockout after 5 failed login attempts
- **Password Policy:** Requires uppercase, lowercase, digit, and special character
- **Forced Password Change:** Default admin must change password on first login
- **Audit Logging:** Timestamped log of all actions for compliance

### Integration

- **OpenAPI 3.0:** Complete API specification for code generation
- **REST/JSON:** Standard interfaces for easy integration
- **Webhook Support:** (Roadmap) Event notifications to external systems

### Mesh Networking (v0.1.0)

- **Multi-Hop Routing:** Automatic failover through mesh peers when controller unreachable
- **Route Discovery:** Dynamic path finding via neighbor broadcast
- **Smart Path Selection:** Routes based on hop count, RTT, and reliability
- **Loop Prevention:** TTL-based hop limits (configurable, default 5 hops)
- **Relay Logging:** Full path tracing for debugging and audit

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                    THEATER OPERATIONS CENTER                        │
│  ┌───────────────┐  ┌─────────────┐  ┌──────────────────────────┐  │
│  │ Mesh          │  │ PostgreSQL  │  │ Web Console              │  │
│  │ Controller    │──│ Database    │  │ (React/TypeScript)       │  │
│  │ (FastAPI)     │  └─────────────┘  └──────────────────────────┘  │
│  └───────┬───────┘                              ▲                   │
│          │                                      │                   │
└──────────┼──────────────────────────────────────┼───────────────────┘
           │ HTTPS/REST                           │
           │ (Heartbeat, Commands)                │
           ▼                                      │
┌──────────────────────────────────────────────────────────────────────┐
│                         TACTICAL EDGE NETWORK                        │
│                                                                      │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐       │
│  │ Vehicle  │◄══►│Dismounted│◄══►│  Sensor  │◄══►│   UAS    │       │
│  │  Node    │    │   Node   │    │   Node   │    │   Node   │       │
│  │ (Agent)  │    │ (Agent)  │    │ (Agent)  │    │ (Agent)  │       │
│  └────┬─────┘    └────┬─────┘    └────┬─────┘    └────┬─────┘       │
│       │               │               │               │              │
│       └───────────────┴───────────────┴───────────────┘              │
│                      UDP Mesh Links                                  │
│            (Route Discovery, Message Relay)                          │
│                                                                      │
│  Multi-Hop Routing: Node A → Node B → Controller                    │
│  When direct path fails, messages relay through peers               │
196: └──────────────────────────────────────────────────────────────────────┘
```

### Technology Stack

| Component          | Technology          | Rationale                                        |
| ------------------ | ------------------- | ------------------------------------------------ |
| Backend Controller | Python / FastAPI    | Widely known, easy to audit, async-native        |
| Database           | PostgreSQL          | Enterprise-grade, strong government track record |
| Web Console        | React / TypeScript  | Industry standard, large talent pool             |
| Node Agent         | Python              | Portable across ARM and x86, easy to modify      |
| Deployment         | Docker / Kubernetes | Standard container orchestration                 |
| API Specification  | OpenAPI 3.0         | Enables code generation and tooling              |

---

## Security and Compliance Posture

### Security Features

- **Transport Security:** All communications over HTTPS/TLS
- **Authentication:** JWT tokens with configurable expiration
- **Authorization:** Role-based access control at every endpoint
- **Audit Trail:** Complete logging of all operator actions with timestamps

### Compliance Considerations

TacticalMesh is designed as a **general-purpose, dual-use platform**:

- ✅ Does not include classified information or algorithms
- ✅ Does not include cryptographic implementations beyond standard TLS
- ✅ Open-source code enables security review and audit
- ✅ Built-in audit logging supports compliance requirements

> **Important:** End-users are responsible for export control compliance. See `docs/compliance-and-export-notes.md` for details.

### Accreditation & Certification Status

> [!WARNING]
> **No Government Accreditation.** TacticalMesh has NOT received any government security accreditation, Authority to Operate (ATO), or certification from any government agency.

**Current Status:**

- ⚠️ No ATO, IL certification, or FedRAMP authorization
- ⚠️ No FIPS-validated cryptography
- ⚠️ No Common Criteria certification

**Design Supports Future Accreditation:**

- ✅ Role-based access control (RBAC) with Admin/Operator/Observer roles
- ✅ Comprehensive audit logging of all operator actions
- ✅ API-first design enabling external monitoring and SIEM integration
- ✅ Clear authentication and authorization boundaries

Organizations deploying in government environments are **solely responsible** for obtaining necessary authorizations. See [SECURITY.md](SECURITY.md) for security policy and vulnerability reporting.

---

## Versioning and Releases

TacticalMesh follows [Semantic Versioning](https://semver.org/):

- **Current Version:** v0.1.0 (Initial public release)
- **Release Tags:** Published on GitHub as `v{major}.{minor}.{patch}`
- **Changelog:** See [CHANGELOG.md](CHANGELOG.md) for detailed release notes

### Version Policy

| Version Range | Stability       | Notes                                    |
| ------------- | --------------- | ---------------------------------------- |
| 0.x.x         | Development     | API may change between minor versions    |
| 1.x.x         | Stable (future) | Backward-compatible within major version |

---

## Running Tests

### Backend Tests

```bash
cd backend
pip install pytest pytest-asyncio httpx aiosqlite
python -m pytest tests/ -v
```

### Agent Tests

```bash
cd agent
pip install pytest
python -m pytest tests/ -v
```

### Frontend Tests

```bash
cd frontend
npm install
npm run test
```

---

## Deployment Quick Start

### Docker Compose (Recommended)

```bash
# Clone the repository
git clone https://github.com/TamTunnel/TacticalMesh.git
cd TacticalMesh

# Start all services
docker-compose up -d

# Verify services are running
docker-compose ps
```

Access points:

- **API:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs
- **Console:** http://localhost:3000

Default credentials: `admin` / `admin123` (password change required on first login)

### Minimal Local Demo

1. **Start the Controller:**

    ```bash
    cd backend
    pip install -r requirements.txt
    uvicorn backend.main:app --reload
    ```

2. **Start a Node Agent:**

    ```bash
    cd agent
    pip install -r requirements.txt
    python -m agent.main --init-config --node-id demo-node-001 --controller http://localhost:8000
    python -m agent.main --config config.yaml
    ```

3. **Start the Console:**
    ```bash
    cd frontend
    npm install
    npm run dev
    ```

---

## Roadmap

### Near-Term (v0.2–0.3)

- [ ] Multi-hop mesh routing between agents
- [ ] Offline command buffering with sync-on-reconnect
- [ ] WebSocket real-time updates in console
- [ ] Prometheus metrics export

### Medium-Term (v0.4–1.0)

- [ ] Geographic visualization (map-based node display)
- [ ] Group-based command targeting
- [ ] Plugin architecture for custom command handlers
- [ ] Integration with common radio APIs (SDR, commercial mesh radios)

### Long-Term (Post-1.0)

- [ ] Distributed controller federation
- [ ] Advanced mesh topology optimization
- [ ] Bandwidth-constrained transport modes
- [ ] Hardware abstraction layer for tactical radios

> **Note:** This roadmap represents potential directions. Actual development priorities will be driven by community needs and contributions.

---

## Contributing

We welcome contributions from the community! Please review our guidelines:

### What We Accept

✅ Bug fixes and improvements  
✅ Documentation enhancements  
✅ New features aligned with project goals  
✅ Test coverage improvements  
✅ Security vulnerability reports (via responsible disclosure)

### What We Cannot Accept

❌ Proprietary or licensed code  
❌ Export-controlled implementations  
❌ Classified information  
❌ Code without appropriate tests or documentation

### Getting Started

1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Submit a Pull Request

See `CONTRIBUTING.md` for full guidelines.

---

## License

TacticalMesh is licensed under the **Apache License 2.0**.

```
Copyright 2024 TacticalMesh Contributors

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

See [LICENSE](LICENSE) for the complete license text.

---

## Contact

- **Repository:** https://github.com/TamTunnel/TacticalMesh
- **Issues:** https://github.com/TamTunnel/TacticalMesh/issues
- **Discussions:** https://github.com/TamTunnel/TacticalMesh/discussions

---

_TacticalMesh — Resilient networking for the tactical edge._
