
import rospy
from std_msgs.msg import Int32

class Publish(object):
    def __init__(self):
        self.pub = rospy.Publisher('/counter', Int32)
    
    def write_data(self, DataToWrite):  
        self.write = self.pub.publish(DataToWrite)  # This has to be a Twist
        
        
class Subscribe(object):
    def __init__(self):  # initialize class
        self.sub = rospy.Subscriber('/counter', Int32, self.read_data)  # tell to the publisher that I use Odometry
        self.ScanData = Int32()
       
    def read_data(self, msg):  #raed data is the function in charge of reading
        self.ScanData = msg