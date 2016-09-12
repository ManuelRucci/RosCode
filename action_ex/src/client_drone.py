#! /usr/bin/env python

import rospy
import time
import actionlib

from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult, ArdroneFeedback
from actionlib_tutorials.msg import FibonacciFeedback, FibonacciResult, FibonacciAction, FibonacciGoal
from geometry_msgs.msg import Twist


nImage = 1
count_second = 0

# definition of the feedback callback. This will be called when feedback
# is received from the action server
# it just prints a message indicating a new message has been received


class Data(object):
    def __init__(self):
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
    
    def Twist_Write(self, Twist):
        self.TwistWrite = self.pub.publish(Twist)

def feedback_callback_IMAGE(feedback):
    global nImage
    print('[Feedback] image n.%d received'%nImage)
    nImage+=1
    
def feedback_callback_FIBONACCI(feedback):
    global count_second
    print('[Feedback] Second '%count_second)
    count_second+=1
    

if __name__ == "__main__":   
    # initializes the action client node
    rospy.init_node('client_drone_node')
    
    var1 = Twist()
    var1.linear.x = 5
    var1.linear.y = 0.0
    var1.linear.z = 0.0
    var1.angular.x = 0.0
    var1.angular.y = 0.0
    var1.angular.z = 0.5
    
    var2 = Twist()
    var2.linear.x = 5
    var2.linear.y = 0.0
    var2.linear.z = 0.0
    var2.angular.x = 0.0
    var2.angular.y = 0.0
    var2.angular.z = 0.5
    
    rospy.loginfo("----done---")
    rate = rospy.Rate(1)
    
    AllData = Data()
    
    TAKE_IMAGE = 1  # DO NOT TAKE IMAGE, 1 TO USE ACTION_SERVER TAKE IMAGE

    if (TAKE_IMAGE == 0):

        # create the connection to the action server
        client = actionlib.SimpleActionClient('/ardrone_action_server', ArdroneAction)
        # waits until the action server is up and running
        client.wait_for_server()
        
        # creates a goal to send to the action server
        goal = ArdroneGoal()    # take picture for 10 s
        goal.nseconds = 20 # indicates, take pictures along 10 seconds
        
        # sends the goal to the action server, specifying which feedback function
        # to call when feedback received
        client.send_goal(goal, feedback_cb=feedback_callback_IMAGE)
        
        ########### Other Stuff while the action is running ##########
        count_time = 0
        while(count_time < 20):
            count_time = count_time + 1
            AllData.Twist_Write(var1)
            if (nImage > 10):
                AllData.Twist_Write(var2)    
                rate.sleep()
        ###############################################################
        
        client.wait_for_result()
    
        print('[Result] State: %d'%(client.get_state()))
    
    else: 
        # create the connection to the action server
        client = actionlib.SimpleActionClient('/fibonacci_as', FibonacciAction)
        # waits until the action server is up and running
        client.wait_for_server()
        
        # creates a goal to send to the action server
        Fib_goal = FibonacciGoal()    
        Fib_goal.order = 3 # fibonacci order
        
        

        # sends the goal to the action server, specifying which feedback function
        # to call when feedback received
        client.send_goal(Fib_goal, feedback_cb=feedback_callback_FIBONACCI)
        
        client.wait_for_result()
        
    
    
    # Uncomment these lines to test goal preemption:
    #time.sleep(3.0)
    #client.cancel_goal()  # would cancel the goal 3 seconds after starting
    
    # wait until the result is obtained
    # you can do other stuff here instead of waiting
    # and check for status from time to time 
    # status = client.get_state()
    # check the client API link below for more info
    
    
    