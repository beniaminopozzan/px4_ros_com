# PX4 - ROS 2 utilities and demos

[![GitHub license](https://img.shields.io/github/license/PX4/px4_ros_com.svg)](https://github.com/PX4/px4_ros_com/blob/master/LICENSE) [![DOI](https://zenodo.org/badge/142936318.svg)](https://zenodo.org/badge/latestdoi/142936318) [![Build and Test package](https://github.com/PX4/px4_ros_com/workflows/Build%20and%20Test%20package/badge.svg?branch=master)](https://github.com/PX4/px4_ros_com/actions)

[![Discord Shield](https://discordapp.com/api/guilds/1022170275984457759/widget.png?style=shield)](https://discord.gg/dronecode)

The `px4_ros_com` package encapsulates:

- [px4_utils](px4_utils/README.md), an utility package to ease the interfacing between ROS 2 and PX4.
- [px4_demo_ccp](px4_demo_cpp/README.md) and [px4_demo_py](px4_demo_py/README.md), two packages containing demo nodes for listening to PX4 messages and performing offboard control.
  
## Supported versions and compatibility

Depending on the PX4 and ROS versions you want to use, you need to checkout the appropriate branch of this package:

| PX4 version   | ROS 2 versions          | branch                                                            |
|---------------|-------------------------|-------------------------------------------------------------------|
| 1.13          | Foxy                    | [release/1.13](https://github.com/PX4/px4_ros_com/tree/release/1.13) |
| 1.14 and  `main` branch        | Foxy - Humble - Rolling | [main](https://github.com/PX4/px4_msgs)                           |

## Install, build and usage

Check [Using colcon to build packages](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html#build-a-package) to understand how this can be built inside a workspace. Check the [PX4 ROS 2 User Guide](https://docs.px4.io/main/en/ros/ros2_comm.html) section on the PX4 documentation for further details on how this integrates PX4 and how to exchange messages with the autopilot.

This package depends on the interface package [px4_msgs](https://github.com/PX4/px4_msgs). Make sure to checkout the appropriate version depending on your target PX4 and ROS versions.

### Full working example -  Offboard Control

Here an example of how to achieve offboard control using the provided demo is presented.
The following setup is considered

- PX4 SITL, we will simulate our drone, a `x500` quadrotor model.
- PX4 version: `main` branch.
- OS: Ubuntu 22.04.
- ROS: Humble. We assume that ROS Humble has been installed on your system in the default location `/opt/ros/humble/` together with the package `ros-dev-tools`.

The guide is divided in three parts

- Fetch, setup and build `PX4-Autopilot`.
- Fetch and build the required ROS packages + the ROS 2 side of the bridge interconnecting ROS to PX4.
- Run the code.

#### Autopilot setup

This step can be skipped if you have already build PX4

1. Clone the `main` branch of PX4:
   ```
   git checkout -b main --recursive https://github.com/PX4/PX4-Autopilot.git ~/PX4-Autopilot
   ```
2. Install the PX4 dependencies:
   ```sh
   ~/PX4-Autopilot/Tools/setup/ubuntu.sh --no-nuttx
   ```
   This will install all the dependencies for building PX4 for simulation and install [Gazebo Garden](https://gazebosim.org/home), the simulator that will be used for our guide.
3. On a new terminal, build the autopilot
   ```sh
   cd ~/PX4-Autopilot
   make px4_sitl
   ```

#### ROS 2 workspace setup

Here we set up a ROS 2 workspace where we will build the required packages.

1. First create the workspace
   ```sh
   mkdir ~/px4_ws/src -p
   cd ~/px4_ws/src
   ```
2. Fetch the packages: we need `px4_msgs`, `px4_ros_com` and the ROS 2 side of the bridge interconnecting ROS to PX4:
   ```sh
   git clone -b main https://github.com/PX4/px4_msgs.git
   git clone -b main https://github.com/PX4/px4_ros_com.git
   git clone https://github.com/eProsima/Micro-XRCE-DDS-Agent.git
   ```
4. Now we can build our workspace
   ```sh
   cd ~/px4_ws/
   source /opt/ros/humble/setup.bash
   colcon build
   ```

#### Run the demo

Now we can run the demo, we need three terminals:

1. Start the simulation (terminal one):
   ```sh
   cd ~/PX4-Autopilot
   make px4_sitl gz_x500
   ```
   The gazebo garden GUI will open.
2. Connect ROS 2 to PX4 (terminal two):
   ```sh
   cd ~/px4_ws
   source install/setup.bash
   MicroXRCEAgent udp4 -p 8888
   ```
3. Start flying (terminal three):
   ```sh
   cd ~/px4_ws
   source install/setup.bash
   ros2 run px4_demo_py offboard_controller
   ```

You will see the drone arming, taking off, reaching an altitude of 5m and then landing.



## Bug tracking and feature requests

Use the [Issues](https://github.com/PX4/px4_ros_com/issues) section to create a new issue. Report your issue or feature request [here](https://github.com/PX4/px4_ros_com/issues/new).

## Questions and troubleshooting

Reach the PX4 development team on the PX4 [Discord Server](https://discord.gg/dronecode).
