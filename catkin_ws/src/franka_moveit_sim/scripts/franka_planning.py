#! /usr/bin/env python

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

# position: 
#     x: 0.05158255291613049
#     y: -0.012858046914186103
#     z: 1.1508234222484397
#   orientation: 
#     x: -0.016674573878376592
#     y: -0.031553846132956045
#     z: 0.23935018585869833
#     w: 0.9702771778773316

# Cria o objeto com a posição home
home_pose = geometry_msgs.msg.Pose()

home_pose.orientation.w =  0.9702771778773316
home_pose.orientation.x = -0.016674573878376592
home_pose.orientation.y = -0.031553846132956045
home_pose.orientation.z =  0.23935018585869833

home_pose.position.x =  0.05158255291613049
home_pose.position.y =  -0.012858046914186103
home_pose.position.z =  1.1508234222484397
group.set_pose_target(home_pose)

# position: 
#     x: -0.5514646039687529
#     y: 0.1116589696660267
#     z: 0.6307402065777306
#   orientation: 
#     x: -0.4678217021185517
#     y: -0.8741991055572292
#     z: 0.13005866393728194
#     w: 0.0018769136076491881

# Cria o objeto com a posição pick
pick_pose = geometry_msgs.msg.Pose()
pick_pose.orientation.w = 0.0018769136076491881
pick_pose.orientation.x = -0.4678217021185517
pick_pose.orientation.y = -0.8741991055572292
pick_pose.orientation.z = 0.13005866393728194

pick_pose.position.x = -0.5514646039687529
pick_pose.position.y = 0.1116589696660267
pick_pose.position.z = 0.6307402065777306

group.set_pose_target(pick_pose)

plan1 = group.plan()
group.go(wait=True)

rospy.sleep(5)

group.set_pose_target(home_pose)

plan1 = group.plan()
group.go(wait=True)

moveit_commander.roscpp_shutdown()