Gmapping for Turtlebot3

How to run:
1. roscore
2. ssh waffle@IP
3. roslaunch turtlebot3_bringup turtlebot3_robot.launch
4. roslaunch turtlebot3_slam turtlebot3_slam.launch
5. roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
6. rosrun map_server map_saver -f ~/map


Navigation 

How to run: 
1. roscore
2. roslaunch turtlebot3_bringup turtlebot3_robot.launch
3. export TURTLEBOT3_MODEL=waffle
4. cd ~/catkin_ws/src/turtlebot3/turtlebot3_navigation/maps/
5. roslaunch turtlebot3_navigation turtlebot3_navigation.launch
6. rviz


Navigation stack

How to run:
1. roscore 
2. ssh waffle@IP
3. roslaunch turtlebot3_bringup turtlebot3_robot.launch
4. roslaunch crazy_robot navigation_tb3.launch
5. rviz
6. python patrol_.py
