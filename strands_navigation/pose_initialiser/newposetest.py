#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Pose, PoseWithCovarianceStamped
from std_msgs.msg import Int16
import time

curr_pos = None
RFID = None

def RFID_callback(tag_loc):
    global RFID
    RFID = tag_loc

def pose_callback(x):
    global curr_pos, RFID
    curr_pos = x
    
    if RFID:
        row = RFID[0]
        col = RFID[1]
    else:
        row = raw_input("RFID tag number (row):  ")
        col = raw_input("RFID tag number (col):  ")
        print
        print "-------------------------------------"
        print 
    
    newpose = PoseWithCovarianceStamped()    
    newpose.header.frame_id = "map"
    newpose.header.stamp.secs = time.time()
    newpose.pose.pose.position.x = float(row)
    newpose.pose.pose.position.y = float(col)
    newpose.pose.pose.orientation = curr_pos.orientation
    newpose.pose.covariance =       [0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 
                                     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                                     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06853891945200942]

    pose_pub.publish(newpose)

if __name__ == "__main__":
    rospy.init_node('next_view_main')
    rospy.Subscriber('/robot_pose',Pose,pose_callback)
    rospy.Subscriber('/RFID_input',Int16,RFID_callback)
    pose_pub = rospy.Publisher('/initialpose',PoseWithCovarianceStamped,queue_size=100)
    rospy.spin()  
