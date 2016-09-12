#! /usr/bin/env python

import rospy
import time

from std_msgs.msg import Int32
from classes import Publish  # import Publish classes


if __name__ == "__main__": 
    
    # Initialize the node 
    rospy.init_node('ex_3_graph_Publisher_node')
    
    PublishWrite = Publish()
    IntToPublish = 10
    
    while not rospy.is_shutdown():
        PublishWrite.write_data(IntToPublish)
        