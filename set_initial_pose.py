#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped, Point
from experiment_coordinates import trial_coordinates
import os
import time

rospy.init_node("set_initial_pose")
pub = rospy.Publisher("initialpose", PoseWithCovarianceStamped, queue_size=100)

while pub.get_num_connections() < 2:
    pass

(start, end, current_trial) = trial_coordinates(os.getenv("PATH_PLANNER_NAME"))

p = PoseWithCovarianceStamped()
p.header.frame_id = "map"
p.header.stamp.secs = time.time()
p.pose.pose = start.pose.pose
p.pose.covariance = [0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06853891945200942]
pub.publish(p)
