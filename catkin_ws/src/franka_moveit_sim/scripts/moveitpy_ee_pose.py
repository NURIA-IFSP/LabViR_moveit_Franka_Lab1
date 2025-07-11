#! /usr/bin/env python

# Utilização do módulo moveit_python para movimentação do robo com base na posição
# do end-effector

import rospy
from moveit_python import MoveGroupInterface
from moveit_msgs.msg import MoveItErrorCodes
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion

rospy.init_node('moveit_python_tutorial', anonymous=True)

move_group = MoveGroupInterface("panda_arm", "panda_link0")

gripper_frame = 'panda_link8'

gripper_poses = [Pose(Point(-0.55143, 0.111, 0.63084), Quaternion(0.46,0.87416, -0.13, -0.00)),
                 Pose(Point(0.5621, 0.02, 0.63075), Quaternion(0.92466, -0.3579, -0.013954, -0.12932))]

gripper_pose_stamped = PoseStamped()
gripper_pose_stamped.header.frame_id = 'panda_link0'

while not rospy.is_shutdown():
    for pose in gripper_poses:
        gripper_pose_stamped.header.stamp = rospy.Time.now()

        gripper_pose_stamped.pose = pose

        result = move_group.moveToPose(gripper_pose_stamped, gripper_frame)

        if result:

            if result.error_code.val == MoveItErrorCodes.SUCCESS:
                rospy.loginfo("Trajectory successfully executed!")
            else:
                rospy.logerr("Arm goal in state: %s",
                             move_group.get_move_action().get_state())
        else:
            rospy.logerr("MoveIt failure! No result returned.")

move_group.get_move_action().cancel_all_goals()
