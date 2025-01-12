The robot_interface package provides a graphical interface to control a robot using ROS2. 
This interface allows the user to move forward or backward the robot by clicking on a graphical window. 
The package is compatible with mobile robots like TurtleBot and uses the /cmd_vel topic to send velocity commands.

# How it works
-The package creates a ROS2 node that initializes a Tkinter-based graphical interface.
-There is a canvas (graphical window) divided into two areas by a horizontal line.By clicking up of the red line of
the graphical window, the robot will move forward, and by clicking down the robot will move backward. 
-When a user clicks on the canvas, the click coordinates are used to determine the command to send to the robot.
-A Twist message is published to the /cmd_vel topic to control the robot's linear velocity.

# Package contents
-robot_control.py: The main script that initializes the graphical user interface and publishes velocity commands.
-setup.py:Configuration file for building and installing the package.
-package.xml:Metadata file for the ROS2 package.

# Package installation
1. Clone the package into the ROS2 interface: cd ~/ros2_ws/src git clone <repository-url>
2. Build the workspace: cd ~/ros2_ws colcon build source install/setup.bash

# How to use
1. Source the TurtleBot3 setup: export TURTLEBOT3_MODEL=burger source /opt/ros/<ros-distro>/setup.bash
2. Launch the simulation world: ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
3. In a new terminal, source the  workspace: source ~/ros2_ws/install/setup.bash
4. Launch de GUI: ros2 run robot_interface robot_control

It will appear a window with a horizontal line dividing into 2 areas.
Click on the upper area to move the robot forward.
Click on the lower area to move the robot backward.
<img width="298" alt="foto1" src="https://github.com/user-attachments/assets/5b376366-d782-4896-82c3-2c17540d4a99" />



