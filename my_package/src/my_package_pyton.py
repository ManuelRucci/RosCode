#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32  #import the Int32 message from std_msgs.msg

rospy.init_node('topic_publisher')
pub = rospy.Publisher('/counter', Int32)
rate = rospy.Rate(2) # set pablish rate to 2Hz
count = 0

while not rospy.is_shutdown(): 
  pub.publish(count)
  
  count += 1
  rate.sleep()  # the publish rate is 2Hz and is keep like that