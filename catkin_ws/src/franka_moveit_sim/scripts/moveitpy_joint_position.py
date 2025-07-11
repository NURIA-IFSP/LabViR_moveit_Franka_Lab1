#! /usr/bin/env python

# Utilização do módulo moveit_python para movimentação do robo com base na posição
# das juntas

import rospy
from moveit_python import MoveGroupInterface
from moveit_msgs.msg import MoveItErrorCodes

rospy.init_node('moveit_python_tutorial', anonymous=True)

move_group = MoveGroupInterface("panda_arm", "panda_link0")

joints = ["panda_joint1", "panda_joint2", "panda_joint3",
          "panda_joint4", "panda_joint5", "panda_joint6", "panda_joint7"]

pose =  [-4.958896245807416e-06, 8.919798419810831e-05, 2.897281519165542, -0.06985355943944306, -9.470555246807635e-05, 3.140033097608248, 0.7280975492132362, 0.0, 0.0]

while not rospy.is_shutdown():

    result = move_group.moveToJointPosition(joints, pose, 0.02)
    if result:

        if result.error_code.val == MoveItErrorCodes.SUCCESS:
            rospy.loginfo("Trajectory successfully executed!")
        else:
            rospy.logerr("Arm goal in state: %s",
                         move_group.get_move_action().get_state())
    else:
        rospy.logerr("MoveIt failure! No result returned.")

move_group.get_move_action().cancel_all_goals()
