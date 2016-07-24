#!/bin/bash

export TSC_TOPICS="
    /scan
    /odom
    /amcl_pose
    /robot_pose
    /current_node
    /current_edge
    /topological_map
    /topological_navigation/Route
    /topological_navigation/Statistics
    /current_node
    /current_edge
    /closest_node
    /map_updates
    /move_base/current_goal
    /move_base/local_costmap/costmap
    /move_base/local_costmap/costmap_updates
    /move_base/DWAPlannerROS/global_plan
    /move_base/DWAPlannerROS/local_plan
    /monitored_navigation/result
"

rosrun mongodb_log mongodb_log.py --nodename-prefix=tsc_logger_ --mongodb-host=localhost --mongodb-port=62345 $TSC_TOPICS
