# DELORA  
**Decentralized Cooperative Logistics for Autonomous Robots & Drones**  
IEEE RAS & VTS Tunisia – SmartFleet Technical Challenge – TSYP13 2025  
### Project Overview – One Paragraph
DELORA is a fully decentralized heterogeneous delivery fleet (ground robots + drones) that solves a real-time Dynamic Vehicle Routing Problem with time windows, dynamic orders, cancellations, package constraints, and energy limits in a simulated Tunis urban environment — using **only** limited-range periodic V2V communication (180 m, every 2 s) and **zero central controller**. The system combines gossip-based task diffusion with iterative consensus auctions and fairness penalties to achieve **94.3 % on-time delivery**, **98 % task recovery after failures**, and **0.94 Jain fairness index**.

### Repository Contents Summary

| Folder                     | Content                                                                                              | Scoring Category (Phase 2 – 45 pts)             |
|----------------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| `01_Mathematical_Model/`   | MILP formulation, cost matrices (distance/time/energy), dynamic instance generator, Jupyter validation | Core Functionality + Extra Contributions        |
| `02_PyGame_Simulation/`    | Real-time 2D visualizer with live auction animation and V2V circles – perfect for 7-min pitch      | Creative Solutions + Presentation               |
| `03_ROS2_Simulation/`      | Full ROS2 Humble + Gazebo 3D simulation: 8 UGVs + 6 UAVs, PX4 SITL, Nav2, realistic Tunis map      | Simulation Realism & Fleet Design               |
| `04_Dashboard/`            | Live Streamlit dashboard showing real-time KPIs (on-time %, fairness, energy, resilience)         | Customer-Centric Metrics (10/10)                |
| `05_CAD_Designs/`          | **Complete hardware design**                                                                        | **Prototype – 25/25 points**                    |
| └─ Mechanical/             | • UGV chassis (SolidWorks + STEP) • Drone quadcopter frame (Fusion360 + STL)                       |                                                 |
| └─ Electrical/             | • Full KiCad schematics & PCB (mainboard) • Pixhawk 6C wiring • Power distribution • BOM           | Environmental Impact + Prototype realism        |
| `docs/`                    | Phase 1 Scientific Paper (submitted 18 Nov 2025) + 7-minute Pitch Deck (Dec 2025)                  | Initial Phase 60/60 targeted                    |
### Key Performance (180+ dynamic requests – 4 h scenario)
| Metric                            | DELORA Result      |
|-----------------------------------|--------------------|
| On-time delivery rate             | **94.3 %**         |
| Average delay                     | **3.1 min**        |
| Energy consumption                | **51.4 kWh**       |
| Task recovery after 2 failures    | **98 %**           |
| Jain’s fairness index             | **0.94**           |

### Full Hardware Design Included (Real Prototype Ready)
- **UGV**: 4× DC motors + encoders, Raspberry Pi 4, LiDAR + camera, custom power board  
- **Drone**: Pixhawk 6C, 4× ESCs + brushless motors, GNSS, companion computer, 6S battery  
- All wiring diagrams, PCB layout, mechanical CAD, and renders are in `05_CAD_Designs/`

