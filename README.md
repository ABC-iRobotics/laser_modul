# ROS package for control the laser on Raspberry Pi

This ROS package implements a ROS Action Server, which uses the `LaserModul.action` Action Message. The laser control module is responsible for turning the laser on and off. The Action Message goal of the `LaserModul.action` is the follow:
- `bool on` - boolean variable to turn on/off the laser

This Message has empty result.
 
The **laser_modul.launch** file is located in **launch** folder. It defines and launches the `laser_modul` ROS node. This node can control the line laser on the Raspberry Pi.

The **LaserModulServer.py** in the **scripts** folder implements the expected functionality.