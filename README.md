# DELORA
**Decentralized Cooperative Logistics for Autonomous Robots & Drones**  
IEEE RAS Tunisia & IEEE VTS Tunisia – SmartFleet Technical Challenge  
TSYP Congress 13th Edition 2025 – Anonymous Student Branch Team

### Project Overview
DELORA is a fully decentralized, heterogeneous delivery fleet (ground robots + drones) that solves a real-time Dynamic Vehicle Routing Problem with time windows in a realistic simulated Tunis urban environment. Vehicles coordinate exclusively through limited-range, periodic V2V communication (180 m range, synchronized every 2 s) — **no central server is ever used**.

Using gossip-based task propagation combined with iterative consensus auctions and fairness-aware bidding, DELORA efficiently handles dynamic orders, cancellations, time-window constraints, package compatibility (weight, fragility, drone-only), vehicle capacity, and energy limitations while maximizing on-time delivery, customer fairness, and system resilience.

### Repository Contents

| Folder                    | What’s Inside                                                                                             |
|---------------------------|-----------------------------------------------------------------------------------------------------------|
| `01_Mathematical_Model/`  | Full MILP formulation, distance/time/energy cost matrices, dynamic order generator, Jupyter validation   |
| `02_PyGame_Simulation/`   | Lightweight 2D real-time simulator with live auction visualization and V2V communication circles         |
| `03_ROS2_Simulation/`     | Complete 3D simulation (ROS2 Humble + Gazebo) – 8 UGVs + 6 UAVs, PX4 SITL, Nav2, realistic Tunis map      |
| `04_Dashboard/`           | Live Streamlit web dashboard showing real-time KPIs: on-time rate, fairness, energy, fleet status        |
| `05_CAD_Designs/`         | **Prototype-ready hardware design**                                                                              |
| ├─ Mechanical/            | UGV chassis (SolidWorks + STEP) • Drone frame (Fusion360 + STL + renders)                                 |
| ├─ Electrical/            | Full KiCad schematics & PCB • Pixhawk 6C wiring • Power distribution • Complete BOM                        |
| ├─ Wiring_Diagrams/       | High-resolution connection diagrams for both UGV and drone (see images below)                             |
| `docs/`                   | Phase 1 Scientific Paper (submitted 18 Nov 2025) • 7-minute Pitch Deck (Dec 2025)                         |
| `media/`                  | Banner, demo videos, renders, and screenshots                                                             |

### Performance Results (180+ dynamic requests – 4-hour scenario)
| Metric                            | Result             |
|-----------------------------------|--------------------|
| On-time delivery rate             | **94.3 %**         |
| Average customer delay            | **3.1 minutes**    |
| Total energy consumption          | **51.4 kWh**       |
| Task recovery after 2 failures    | **98 %**           |
| Jain’s fairness index (waiting time) | **0.94**        |

### Hardware – Ready for Real-World Build
**UGV**  
4× DC motors + encoders • Raspberry Pi 4 • RPLIDAR A1 • Camera • Custom power board • 6S LiPo

**Drone**  
Pixhawk 6C • 4× brushless motors & ESCs • GNSS module • Companion computer • Telemetry • 6S battery

All mechanical CAD files, electrical schematics, PCB layouts, wiring diagrams, and BOM are included in `05_CAD_Designs/`.
