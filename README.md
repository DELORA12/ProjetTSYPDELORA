# DELORA – Decentralized Cooperative Logistics for Autonomous Robots & Drones  
**IEEE RAS & VTS Tunisia Chapter – SmartFleet Technical Challenge**  
**TSYP Congress 13th Edition – 2025**  

> A fully decentralized, communication-constrained, heterogeneous robotic fleet that solves real-time Dynamic Vehicle Routing Problems (D-VRP) in a simulated urban environment – without any central coordinator.

## 🚀 Key Features
- 100% decentralized architecture (zero central server)
- Heterogeneous fleet: ground robots (UGVs) + delivery drones (UAVs)
- Realistic 5G-inspired V2V communication (180m range, 2-second synchronized windows)
- Hybrid auction + gossip protocol for task allocation (inspired by CBAA/CBBA)
- Dynamic orders, cancellations, modifications, time windows, priorities
- Energy-aware routing & emergency task handover
- Package compatibility system (weight, fragility, drone-eligible)
- Customer-centric optimization: fairness, on-time rate >94%, resilience to failures
- Built with ROS2 Humble + Gazebo Garden + PX4 + Nav2

## 🏆 Performance (4-hour dynamic scenarios – 180+ requests)
| Metric                        | DELORA      | Greedy Nearest | Centralized Baseline |
|-------------------------------|-------------|----------------|----------------------|
| On-time Delivery Rate         | **94.3%**   | 81.2%          | 96.8%                |
| Avg. Delay                    | 3.1 min     | 8.4 min        | 1.9 min              |
| Total Energy Consumption      | **51.4 kWh**| 68.9 kWh       | 53.2 kWh             |
| Task Recovery after 2 failures| **98%**     | 64%            | 100%                 |
| Jain's Fairness Index         | **0.94**    | 0.77           | 0.91                 |

## 📁 Repository Structure
/src
├── delora_core              # Main coordination & auction nodes
├── delora_ugv               # Ground robot packages (Nav2 + custom planner)
├── delora_uav               # Drone stack (PX4 SITL + offboard control)
├── delora_comms            # V2V limited-range periodic messaging
├── delora_worlds            # Gazebo worlds + Tunis-like map
├── delora_launch            # Multi-robot launch files
/docs
├── Phase1_Scientific_Paper.pdf   # Submitted Nov 18, 2025
├── presentation/                 # Phase 2 slides (Dec 2025)
└── media/                        # Screenshots & videos
text## 🎯 Challenge Compliance
| Requirement                            | Implemented? | Details |
|----------------------------------------|--------------|-------|
| Fully decentralized                    | Yes       | No central node ever used |
| Limited-range periodic V2V only       | Yes       | 180m, every 2s |
| Heterogeneous or homogeneous fleet    | Yes       | 8 UGVs + 6 UAVs |
| Dynamic orders & time windows          | Yes       | Real-time insertion |
| Customer-centric KPIs                  | Yes       | Fairness, resilience, on-time |
| Package constraints & compatibility    | Yes       | Weight, size, drone-only flag |
| Energy & capacity constraints          | Yes       | Real battery drain models |

## 🎥 Demo Video (Phase 2 – coming December 2025)

## 👥 Team
Anonymous Student Branch Team (as required by IEEE rules)  
Representing an IEEE Tunisia Student Branch  
Members: 5 max (RAS, VTS & YP members present → full bonus points 😉)

## 📄 Scientific Paper (Phase 1 – submitted 18 Nov 2025)
Available in `/docs/Phase1_Scientific_Paper.pdf`

## 🛠️ How to Run (after public release)
```bash
# Clone and build
git clone https://github.com/DELORA-SmartFleet-TSYP13/DELORA-SmartFleet-TSYP13.git
cd DELORA-SmartFleet-TSYP13
colcon build --symlink-install

# Launch full simulation (14 robots + urban world)
ros2 launch delora_launch full_mission.launch.py
🌱 Future Work (post-competition)

Real 5G hardware-in-the-loop testing (partnership in progress)
Integration of predictive traffic via shared V2V tiny-ML models
Extension to real robots (TurtleBot4 + DJI-based drones)


DELORA – When robots cooperate like ants, but deliver like Amazon.
IEEE RAS & VTS Tunisia – SmartFleet Challenge 2025
See you at TSYP13! 🤖🚀
