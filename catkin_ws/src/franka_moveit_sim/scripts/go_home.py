#! /usr/bin/env python

# Utilização do módulo moveit_python para movimentação do robo com base na posição
# das juntas - Script go_home.py

import rospy
from moveit_python import MoveGroupInterface
from moveit_msgs.msg import MoveItErrorCodes

rospy.init_node('moveit_python_tutorial', anonymous=True)

move_group = MoveGroupInterface("panda_arm", "panda_link0")

joints = ["panda_joint1", "panda_joint2", "panda_joint3",
          "panda_joint4", "panda_joint5", "panda_joint6", "panda_joint7"]

# Home position - arm up
pose =  [-4.96e-06, 9.00e-05, 2.90, -0.07, -9.50e-05, 3.14, 0.73, 0.0, 0.0]

result = move_group.moveToJointPosition(joints, pose, 0.02)

if result:

    if result.error_code.val == MoveItErrorCodes.SUCCESS:
        rospy.loginfo("Trajectory successfully executed!")
    else:
        rospy.logerr("Arm goal in state: %s",
        move_group.get_move_action().get_state())
else:
    rospy.logerr("MoveIt failure! No result returned.")