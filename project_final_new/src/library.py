#! /usr/bin/env python

import rospy
import math

from geometry_msgs.msg import Twist  #import the Int32 message from std_msgs.msg
from sensor_msgs.msg import Imu      # import imu structure data
from nav_msgs.msg import Odometry    # import Odometry data


class Data(object):
    def __init__(self):
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
        self.sub = rospy.Subscriber('/odom', Odometry, self.odom_read) 
        self.sub = rospy.Subscriber('/imu', Imu, self.imu_read) 
        self.OdomRead = Odometry()
        self.ImuRead = Imu()
    
    def odom_read(self, OdomData):
        self.OdomRead = OdomData
        
    def imu_read(self, ImuData):
        self.ImuRead = ImuData
        
    def Twist_Write(self, Twist):
        self.TwistWrite = self.pub.publish(Twist)
        
def norma(vect):
    return math.sqrt(vect.x*vect.x+vect.y*vect.y+vect.z*vect.z)
    

class TwistType(object):
    def __init__(self):
        self.init_go_straight()
        self.init_rotate_right()
        self.init_rotate_left()
        self.init_stop()
        
    def init_go_straight(self):
        self.GO_STRAIGHT = Twist()
        self.GO_STRAIGHT.linear.x  = 0.05
        self.GO_STRAIGHT.linear.y  = 0.0
        self.GO_STRAIGHT.linear.z  = 0.0
        self.GO_STRAIGHT.angular.x = 0.0
        self.GO_STRAIGHT.angular.y = 0.0
        self.GO_STRAIGHT.angular.z = 0.0
        
    def init_rotate_left(self):
        self.GO_LEFT = Twist()
        self.GO_LEFT.linear.x  = 0.0
        self.GO_LEFT.linear.y  = 0.0
        self.GO_LEFT.linear.z  = 0.0
        self.GO_LEFT.angular.x = 0.0
        self.GO_LEFT.angular.y = 0.0
        self.GO_LEFT.angular.z = 1.7
        
    def init_rotate_right(self):
        self.GO_RIGHT = Twist()
        self.GO_RIGHT.linear.x  = 0.0
        self.GO_RIGHT.linear.y  = 0.0
        self.GO_RIGHT.linear.z  = 0.0
        self.GO_RIGHT.angular.x = 0.0
        self.GO_RIGHT.angular.y = 0.0
        self.GO_RIGHT.angular.z = -1.7
        
    def init_stop(self):
        self.STOP = Twist()
        self.STOP.linear.x  = 0.0
        self.STOP.linear.y  = 0.0
        self.STOP.linear.z  = 0.0
        self.STOP.angular.x = 0.0
        self.STOP.angular.y = 0.0
        self.STOP.angular.z = 0.0
    
    def get_direction(self, direction):
        if (direction == "GO_STRAIGHT"):
            return self.GO_STRAIGHT
        elif (direction == "ROTATE_LEFT"):
            return self.GO_LEFT
        elif (direction == "ROTATE_RIGHT"):
            return self.GO_RIGHT
        elif (direction == "STOP"):
            return self.STOP


def MotionPlanning(STATE):
    
    if ( STATE == 1 ):
        return "GO_STRAIGHT"
        
    elif (STATE == 2):
        return "STOP"
                
    elif ( STATE == 3):
        return "ROTATE_RIGHT"
            
    elif ( STATE == 4):
        return "STOP"
        
    elif ( STATE == 5):
        return "GO_STRAIGHT"
    
    elif ( STATE == 6):
        return "STOP"
            
    elif ( STATE == 7 ):
        return "ROTATE_LEFT"
    
    elif ( STATE == 8):
        return "STOP"
            
    elif (STATE == 9):
        return "GO_STRAIGHT"
            
    elif (STATE == 10):
        return "STOP"
