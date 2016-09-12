#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry 

def read_data(msg):  #raed data is the function in charge of reading
  
  print 'position.x', msg.pose.pose.position.x
  print 'orientation.x',msg.pose.pose.orientation.x
  
  print 'twist.linear.x', msg.twist.twist.linear.x
  print 'twist.angular.y', msg.twist.twist.angular.x
  
rospy.init_node('ex_2_node')
sub = rospy.Subscriber('/odom', Odometry, read_data)  # tell to the publisher that I use Odometry
rospy.spin()