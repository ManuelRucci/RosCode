#! /usr/bin/env python

import rospy
import time
import tf
import math

from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Twist  #import the Int32 message from std_msgs.msg
from sensor_msgs.msg import Imu      # import imu structure data
from nav_msgs.msg import Odometry    # import Odometry data
from geometry_msgs.msg import Quaternion


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
        self.init_go_right()
        self.init_go_left()
        self.init_stop()
        
    def init_go_straight(self):
        self.GO_STRAIGHT = Twist()
        self.GO_STRAIGHT.linear.x = 90   #50
        self.GO_STRAIGHT.linear.y  = 45
        self.GO_STRAIGHT.linear.z  = 0.0
        self.GO_STRAIGHT.angular.x  = 0.0
        self.GO_STRAIGHT.angular.y = 0.0
        self.GO_STRAIGHT.angular.z = 0.0
        
    def init_go_left(self):
        self.GO_LEFT = Twist()
        self.GO_LEFT.linear.x = 60
        self.GO_LEFT.linear.y  = 0.0
        self.GO_LEFT.linear.z  = 0.0
        self.GO_LEFT.angular.x  = 0.0
        self.GO_LEFT.angular.y = 0.0
        self.GO_LEFT.angular.z = 0.8
        
    def init_go_right(self):
        self.GO_RIGHT = Twist()
        self.GO_RIGHT.linear.x = 60
        self.GO_RIGHT.linear.y  = 0.0
        self.GO_RIGHT.linear.z  = 0.0
        self.GO_RIGHT.angular.x  = 0.0
        self.GO_RIGHT.angular.y = 0.0
        self.GO_RIGHT.angular.z = -0.8
        
    def init_stop(self):
        self.STOP = Twist()
        self.STOP.linear.x = 0.0
        self.STOP.linear.y  = 0.0
        self.STOP.linear.z  = 0.0
        self.STOP.angular.x  = 0.0
        self.STOP.angular.y = 0.0
        self.STOP.angular.z = 0.0
    
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
        
    elif (STATE == 2):
        return "STOP"
                
    elif ( STATE == 3):
        return "GO_RIGHT"
            
    elif ( STATE == 4):
        return "STOP"
        
    elif ( STATE == 5):
        return "GO_STRAIGHT"
    
    elif ( STATE == 6):
        return "STOP"
            
    elif ( STATE == 7 ):
        return "GO_LEFT"
    
    elif ( STATE == 8):
        return "STOP"
            
    elif (STATE == 9):
        return "GO_STRAIGHT"
            
    elif (STATE == 10):
        return "STOP"


if __name__ == "__main__": 

    rospy.init_node('project_final_node')
    
    AllData = Data()           # create object DATA (Subscribe (read) data from the sensor reading from a topic) 
    MOVEMENT = TwistType()     # create object movement (GO_STRAIGHT, GO_LEFT, GO_RIGHT, STOP)
    
    STATE = 1                 # initiliaze Action  
    #print 'Action', MotionPlanning(STATE)
    #time.sleep(5)
    count = 0                  # value that indicate how many times the accelearation has to be bigger than threshold_mod to detect crash
    while not rospy.is_shutdown():   # until python is not shut down CTRL+C
        
        #print 'PositionOdom' , AllData.OdomRead.pose.pose.position
        #print 'QuaternionOrientationOdom' , AllData.OdomRead.pose.pose.orientation
        #print 'QuaternionOrientationImu' , AllData.ImuRead.orientation
        
        euler = tf.transformations.euler_from_quaternion( [AllData.OdomRead.pose.pose.orientation.x, AllData.OdomRead.pose.pose.orientation.y,AllData.OdomRead.pose.pose.orientation.z, AllData.OdomRead.pose.pose.orientation.w])
        
        roll = (euler[0]*180)/3.14
        pitch = (euler[1]*180)/3.14
        yaw = (euler[2]*180)/3.14
        
        
        #print 'pitch', pitch
        #print 'yaw', yaw
        
        #time.sleep(5)
        
        ############ Strategy ##############
        # 1) Go straight until the collision, 
        # 2) Go to the right until collision
        # 3) Go straight until collision 
        # 4) Go left until collision
        # 5) Go straight until collision
        ####################################
        
        # Detect crash looking at acceleration IMU
        Modulo = norma( AllData.ImuRead.linear_acceleration)       # Get acceleration Module (norm) print 'Mod', Modulo
        threshold_mod = 13           #  13                                          # Set threshold
        #threshold_acc_max = 800
        threshold_acc_min = 500
        
        print 'STATE', MotionPlanning(STATE)
        print 'MOD', Modulo
        if (Modulo > threshold_mod ):
            count = count + 1
            
            if ( (count > threshold_acc_min) ): #and ( count < threshold_acc_max )):
                print 'STATE', MotionPlanning(STATE)
                count = 0
                STATE = STATE + 1
                
                if (STATE == 11 ):
                    STATE = 1
        
        AllData.Twist_Write(MOVEMENT.get_direction(MotionPlanning(STATE)))
        
        if (STATE % 2 == 0):
            time.sleep(2)
        else: time.sleep(1)
        
        


