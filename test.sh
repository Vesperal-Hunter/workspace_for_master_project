#!/bin/bash

for ((i=0; i<300; i++));do
    rosrun topological_navigation topological_navigation_tester_critical.py
done
