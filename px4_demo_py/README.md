# px4_demo_py

This packages offers ROS 2 python demo nodes for performing offboard control of a PX4-powered vehicle.

## Available nodes

### offboard_controller

A simple [offboard position controller](./px4_demo_py/offboard_control.py), it manages the vehicle switching to [offboard control](https://docs.px4.io/main/en/flight_modes/offboard.html) and arming, then it control the vehicle through [TrajectorySetpoint](https://github.com/PX4/PX4-Autopilot/blob/main/msg/TrajectorySetpoint.msg) messages.

#### Limitations

- When sending [VehicleCommand](https://github.com/PX4/PX4-Autopilot/blob/7ed90c6d0c48bf6b5c19f5b54b7b5843266f400c/msg/VehicleCommand.msg) messages, for arming and change of modes, the `target_system` is currently set to `1`. This limits the node to communicate to vehicles having MAVLINK system_id ([MAV_SYS_ID](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#MAV_SYS_ID) as PX4 parameter) equal to one.