# ROS web Simple example

In this project there is a simple example how to use [rosbridge serve](http://wiki.ros.org/rosbridge_suite)r ands roslibjs to comunicate with ROS using yout web browser.
The final objective is to create a simple html as viewer that allow the brower to show param about the robot suscribed by means of Ros and it can publish specific data to simulate robot.

In this case, the robot will be a turtle thanks to turtlesim provide for ROS.

## New Version

Currently, It's being has implemented two turtles ( 2 robots ) to improve the work of interaction between robots.

## Requeriments

Assumes the following tools:

 - [ROS Kinetic](http://wiki.ros.org/kinetic/Installation) running on Ubuntu 16.04 
 - Catkin tools

## Help

It's important to know the environment around ROS and its basic structure.
Read followings documents: [DOC Folder](https://github.com/manujose94/ROS-web-and-python/tree/master/doc)


## Simulator

**TurtleSim**, this must be launch through the next command:

```sh
student@ubuntu:~$ rosrun turtlesim turtlesim_node build-essential
```
## Structure
Ros workspace  is **catkin_ws** and workspace where contain this example is **robot_gui_bridge** . Forto know as started ros project and starting to create your code , must look at the bottom of the page.

    .
    ├── build
    │   ├── catkin_tools_prebuild
    │   │   ├── Makefile
    │   │   ├── package.xml
    │   │   └── test_results
    │   └── robot_gui_bridge
    ├── devel
    └── src
        ├── CMakeLists.txt -> /opt/ros/kinetic/share/catkin/cmake/toplevel.cmake
        └── robot_gui_bridge
            ├── build
            │   ├── roslib.js
            │   └── roslib.min.js
            ├── CMakeLists.txt
            ├── gui
            │   ├── gui.html
            │   └── w3.css
            ├── launch
            │   └── websocket.launch
            └── package.xml
## Creating a workspace
```shell
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin create pkg robot_gui_bridge --catkin-deps rosbridge_server
cd ~/catkin_ws
```
You could install the package manually using a command `apt-get install ros-melodic-rosbridge-server`
## Launch example

### Before starting

```sh
sudo apt-get install ros-kinetic-tf2-tools
````
This is necessary because it must launch two turtlesim at once


Before to launch example you mitgh be make sure you have done the folllow commands:
```sh
catkin build # or catkin_make
source devel/setup.bash
```
Launch:
````sh
student@ubuntu:~/catkin_ws$ roslaunch robot_gui_bridge websocket.launch
````
````sh
student@ubuntu:~$ rosrun turtlesim turtlesim_node build-essential
````
## Starting project in ROS
The next folder is created automatically when the installation of ROS is successful
````sh
student@ubuntu:~/catkin_ws/
student@ubuntu:~/catkin_ws/src$ catkin_create_pkg beginner_tutorials std_msgs rospy roscpp
````
After to create a package, you return to root project folder and:
````sh
student@ubuntu:~$ cd ~/catkin_ws
student@ubuntu:~/catkin_ws$ catkin build
student@ubuntu:~/catkin_ws$ . ~/catkin_ws/devel/setup.bash
````
If the codec that we want to launch if **.py**, add it ejecutable permission:
student@ubuntu:~/catkin_ws/src/beginner_tutorials/src$ sudo chmod +x goto.py
### Launch
#### 1.   Initialize
````sh
student@ubuntu:~$ roscore
````
#### 2. (goto.py works over turtle simulator)
````sh
student@ubuntu:~$ rosrun beginner_tutorials  beginner_tutorials/src/goto.py
````
  
### Useful ROS commands
````sh
 student@ubuntu:~$ rostopic list
/client_count
/connected_clients
/rosout
/rosout_agg
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose
````
````
student@ubuntu:~$ rostopic info /turtle1/pose
Type: turtlesim/Pose

Publishers: 
 * /turtlesim (http://ubuntu:37855/)

Subscribers: None
````

