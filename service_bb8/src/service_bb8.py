#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist


class Data(object):
    def __init__(self):
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)

    def Twist_Write(self, Twist):
        self.TwistWrite = self.pub.publish(Twist)

class TwistType(object):
    def __init__(self):
        self.init_go_straight()
       
    def init_go_straight(self):
        self.GO_STRAIGHT = Twist()
        self.GO_STRAIGHT.linear.x = 0.5
        self.GO_STRAIGHT.linear.y  = 0.0
        self.GO_STRAIGHT.linear.z  = 0.0
        self.GO_STRAIGHT.angular.x  = 0.0
        self.GO_STRAIGHT.angular.y = 0.0
        self.GO_STRAIGHT.angular.z = 0.0  
        
    def get_direction(self, direction):
        if (direction == "GO_STRAIGHT"):
            return self.GO_STRAIGHT
        elif (direction == "GO_LEFT"):
            return self.GO_LEFT
        elif (direction == "GO_RIGHT"):
            return self.GO_RIGHT
        elif (direction == "STOP"):
            return self.STOP
            
def MotionPlanning(STATE):
    
    if ( STATE == 1 ):
        return "GO_STRAIGHT"
                
    elif ( STATE == 2):
        return "GO_RIGHT"
            
    elif ( STATE == 3):
        return "GO_STRAIGHT"
            
    elif ( STATE == 4 ):
        return "GO_LEFT"
            
    elif (STATE == 5):
        return "GO_STRAIGHT"
            
    else:
        return "STOP"

def my_callback(request):
    print "My_callback has been called"
    
    AllData = Data()
    MOVEMENT = TwistType() 
    STATE = 1
    
    rate = rospy.Rate(2) # set pablish rate to 2Hz
    count = 0
    
    while(count < 10):
        AllData.Twist_Write(MOVEMENT.get_direction(MotionPlanning(STATE)))
        count = count +1 
        rate.sleep()
    
    
    return EmptyResponse() # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split())) 

  
if __name__ == "__main__":      
    rospy.init_node('service_bb8_node') 
    my_service = rospy.Service('/my_service', Empty , my_callback) # create the Service called my_service with the defined callback
    
    rospy.spin()  # Ros loop that update everything
    
    
    
    
        
        
        
        
        
        
        
        
        