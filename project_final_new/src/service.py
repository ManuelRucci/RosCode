#! /usr/bin/env python

import rospy
import time

from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.

#import tf
#from tf.transformations import euler_from_quaternion
#from geometry_msgs.msg import Quaternion

from library import Data
from library import TwistType
from library import MotionPlanning
from library import norma


def my_callback(request):
    rospy.loginfo("----------Service has been called---------")
    
    ############ Strategy ##############
        # 1) Go straight until the collision, 
        # 2) Go to the right until collision
        # 3) Go straight until collision 
        # 4) Go left until collision
        # 5) Go straight until collision
    ####################################
    
    AllData = Data()
    MOVEMENT = TwistType() 
    STATE = 1
    
    rate = rospy.Rate(0.5)         # set pablish rate to 1Hz
    count_time = 0               # time counter
    threshold_mod = 3           #  Acceleration norm threshold
    time_stop = 0
    go = 0
    
    rospy.loginfo(MotionPlanning(STATE))
    
    while(time_stop < 100):      # if time stop greater than 100
        
        rospy.loginfo(MotionPlanning(STATE))
        
        time_stop = time_stop + 1
        count_time = count_time + 1
        
        # Compute Module
        Modulo = norma( AllData.ImuRead.linear_acceleration) 
        
        if (Modulo > threshold_mod or count_time>10):
            count_time = 0
            STATE = STATE + 1
            
        if (STATE == 11 ):
            STATE = 1
        
        rospy.loginfo(STATE)
        rospy.loginfo(Modulo)
        
        AllData.Twist_Write(MOVEMENT.get_direction(MotionPlanning(STATE)))
        
        if (STATE % 2 == 0):
            go = go + 1
            if (go == 2):
                go = 0
                STATE = STATE + 1
            
        count_time = count_time +1 
        rate.sleep()
    
    return EmptyResponse() 

  
if __name__ == "__main__":      
    rospy.init_node('service_node') 
    my_service = rospy.Service('/my_service', Empty , my_callback) # create the Service called my_service with the defined callback
    
    rospy.spin()  # Ros loop that update everything

  