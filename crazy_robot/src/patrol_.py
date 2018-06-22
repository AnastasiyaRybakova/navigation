#!/usr/bin/env python

import rospy
import actionlib

import math
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import quaternion_from_euler

waypoints = [
    #  x    y   theta
    [0.60, 0.20, 0],
    [3.00, 1.00, 340],
    [5.85, -0.80, 270],
    [8.00, 0.00, 45],
    [6.00, 1.40, 90],
    [0.60, 0.20, 0]
]


def goal_pose(pose):
    goal_pose = MoveBaseGoal()
    goal_pose.target_pose.header.frame_id = 'map'
    goal_pose.target_pose.pose.position.x = pose[0]
    goal_pose.target_pose.pose.position.y = pose[1]
    goal_pose.target_pose.pose.position.z = 0.0

    ori= quaternion_from_euler(0., 0., pose[2]*math.pi/180.)

    goal_pose.target_pose.pose.orientation.x = ori[0]
    goal_pose.target_pose.pose.orientation.y = ori[1]
    goal_pose.target_pose.pose.orientation.z = ori[2]
    goal_pose.target_pose.pose.orientation.w = ori[3]

    return goal_pose


if __name__ == '__main__':
    rospy.init_node('patrol')

    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()


    for pose in waypoints:
        goal = goal_pose(pose)
        client.send_goal(goal)
        client.wait_for_result()
