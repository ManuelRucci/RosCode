#! /usr/bin/env python

import rospy
import time

from std_msgs.msg import Int32
from  classes import Subscribe   #import subscribe classes

        
if __name__ == "__main__":    
    
    # Initialize the node 
    rospy.init_node('ex_3_graph_Subscriber_node')
    
    SubscribeRead = Subscribe()
    
    while not rospy.is_shutdown():
        plot = SubscribeRead.ScanData    
        
