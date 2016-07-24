#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Pose,PoseWithCovarianceStamped
from rospy import rostime

curr_pos = None

def pose_callback(x):
    global curr_pos
    curr_pos = x
    set_pose()

def set_pose():       
    newpose = PoseWithCovarianceStamped()    
    newpose.header.frame_id = "map"
    newpose.header.stamp.secs = rospy.rostime.time()
    newpose.pose.pose.position.x = -10
    newpose.pose.pose.position.y = -10
    newpose.pose.pose.orientation.x = 0
    newpose.pose.pose.orientation.y = 0
    newpose.pose.pose.orientation.z = 0.999381560105
    newpose.pose.pose.orientation.w = -0.035163863861
    newpose.pose.covariance =       [0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 
                                     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                                     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06853891945200942]

    pose_pub.publish(newpose)

if __name__ == "__main__":
    rospy.init_node('Start')
    rospy.Subscriber('/robot_pose',Pose,pose_callback)
    pose_pub = rospy.Publisher('/initialpose',PoseWithCovarianceStamped,queue_size=100)
    rospy.spin()
