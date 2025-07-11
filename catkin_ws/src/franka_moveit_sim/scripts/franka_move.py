#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

#  Allow the communicattion with the MoveIt RViz interface.
moveit_commander.roscpp_initialize(sys.argv)

# Innitialize the ROS node
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

# Create the robotCommander object - interface with the robot
robot = moveit_commander.RobotCommander()
# Create a PlanningSceneInterface object, which is, basically, an interface to the world that surrounds the robot.
scene = moveit_commander.PlanningSceneInterface()    
# create a MoveGroupCommander object, which is an interface to the manipulator group of joints that we defined when we created the MoveIt package
group = moveit_commander.MoveGroupCommander("panda_arm")
# Define a publisher - defining a Topic Publisher, which will publish into the /move_group/display_planned_path topic. By publishing into this topic,
# we will be able to visualize the planned motion through the MoveIt RViz interface.
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)

# Create a pose object - mensagem que será enviada para o grupo como objetivo "goal"
pose_target = geometry_msgs.msg.Pose()
pose_target.orientation.w = 0.3
pose_target.position.x = 0.5
pose_target.position.y = 0.5
pose_target.position.z = 0.5
group.set_pose_target(pose_target)

# Diz ao manipulador para criar o plano de movimentação. Se conseguir será exibido no RViz
plan1 = group.plan()

# Executa a trajetoria calculada
group.go(wait=True)

rospy.sleep(5)

moveit_commander.roscpp_shutdown()
