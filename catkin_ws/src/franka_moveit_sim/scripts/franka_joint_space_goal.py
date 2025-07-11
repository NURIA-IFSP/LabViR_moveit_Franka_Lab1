#! /usr/bin/env python

# Script para movimentação de uma junta específica para uma determinada posição

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

# Obtenção dos valores atuais das juntas - posicao atual do robo
group_variable_values = group.get_current_joint_values()

# Ajuste da posição da junta de interesse, no caso a junta 5 (panda_joint_6) e o valor desejado - 3.14
group_variable_values[5] = 3.14
group.set_joint_value_target(group_variable_values)

# Planeje a trajetoria
rospy.loginfo("Planejando a trajetoria...")
plan2 = group.plan()

# Va para a nova posiçao
rospy.loginfo("Executando a trajetoria...")
group.go(wait=True)

rospy.sleep(5)

moveit_commander.roscpp_shutdown()
