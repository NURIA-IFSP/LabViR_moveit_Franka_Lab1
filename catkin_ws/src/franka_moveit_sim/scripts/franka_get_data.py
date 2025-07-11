#! /usr/bin/env python

# É possivel a obtenção de dados importantes sobre a simulação utilizando código

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
group = moveit_commander.MoveGroupCommander("panda_arm")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)

# Obtenção do reference frame para um determinado grupo
print ("Reference frame: %s" % group.get_planning_frame())

# Obtenção do grupo do ende effector
print ("End effector: %s" % group.get_end_effector_link())

# Obtenção dos grupos do robo
print ("Robot Groups:")
print (robot.get_group_names())

# Valor atual das juntas
print ("Current Joint Values:")
print (group.get_current_joint_values())

# Pose atual
print ("Current Pose:")
print (group.get_current_pose())

# Estado atual do robo
print ("Robot State:")
print (robot.get_current_state())
