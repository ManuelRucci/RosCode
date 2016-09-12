#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist #import the Int32 message from std_msgs.msg

rospy.init_node('ex_1_node')
pub = rospy.Publisher('/cmd_vel', Twist)
rate = rospy.Rate(2) # set pablish rate to 2Hz

var = Twist()
var.linear.x = 0.5 #m/s
var.angular.z  = 0.8 # rad/s

while not rospy.is_shutdown(): 
  pub.publish(var)
  
  rate.sleep()  # the publish rate is 2Hz and is keep like that