#! /usr/bin/env python

import rospy
import sys 

from std_srvs.srv import Empty, EmptyResponse, EmptyRequest # you import the service message python classes generated from Empty.srv.

if __name__ == "__main__":   
    rospy.init_node('client_bb8_node')                # initialise a ROS node with the name service_client
    
    rospy.loginfo('waiting service')
    
    rospy.wait_for_service('/my_service') # wait for the service client /gazebo/delete_model to be running
    
    rospy.loginfo('finish wait service')
    
    SendRequest = rospy.ServiceProxy('/my_service', Empty) # create the connection to the service
    
    var = EmptyRequest()
    
    result = SendRequest(var) # send through the connection the name of the object to be deleted by the service
    
    rospy.loginfo('Success') # print the result given by the service calledSettings