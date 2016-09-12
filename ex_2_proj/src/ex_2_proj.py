#! /usr/bin/env python

import rospy
import time


from geometry_msgs.msg import Twist  # import Trist message to write
from sensor_msgs.msg import LaserScan


#def read_data(msg):  #raed data is the function in charge of reading
 #   ScanData = msg.ranges
  #  return ScanData
    
# Create class (object) a Twist object to write
class TwistObject:
    def __init__(self):
        self.pub = rospy.Publisher('/cmd_vel', Twist)
    
    def write_data(self, DataToWrite):  
        self.write = self.pub.publish(DataToWrite)  # This has to be a Twist
  

# Create a Class (an object Laser) to read every time data from the Laser
class LaserObject:
    def __init__(self):  # initialize class
        self.sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, self.read_data)  # tell to the publisher that I use Odometry
        self.ScanData = LaserScan()
       
    def read_data(self, msg):  #raed data is the function in charge of reading
        self.ScanData = msg
    
    
    
if __name__ == "__main__":    
    
    # Initialize the node 
    rospy.init_node('ex_2_proj_node')
    
    # create Laser object
    MyLaserObject = LaserObject()  # get laser data
    #print 'DATA', MyLaserObject.ScanData.ranges  # print data scanned by the laser
    MyTwistObject = TwistObject()

    TwistToWrite = Twist();

    #print 'SIZEEE',sys.getsizeof(MyLaserObject.ScanData.ranges)
    
    time.sleep(5) # wait that the arry is load
    n = 360 # number of the middle of the array to see in front
    print 'Front', MyLaserObject.ScanData.ranges[n]
    
    while not rospy.is_shutdown(): 
       # print 'Front', MyLaserObject.ScanData.ranges[n]
          
        if MyLaserObject.ScanData.ranges[n]>3:
            TwistToWrite.linear.x = 0.5 #m/s
            TwistToWrite.angular.z = 0.0 #m/s
            MyTwistObject.write_data(TwistToWrite)
        else:
            TwistToWrite.linear.x = -0.5 #m/s
            TwistToWrite.angular.z = -0.3 #m/s
            MyTwistObject.write_data(TwistToWrite)
           
        

#time.sleep(5)  # sleep for 5 times
#print 'DATA', MyLaserObject.ScanData.ranges
# create a Twist object
#MyTwistObject = TwistObject()

