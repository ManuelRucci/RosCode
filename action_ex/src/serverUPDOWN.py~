#! /usr/bin/env python

import rospy

import actionlib

from actionlib_tutorials.msg import UP_DOWNFeedback, UP_DOWNResult, UP_DOWNAction
from geometry_msgs.msg import Twist

class UP_DOWNClass(object):
    
  # create messages that are used to publish feedback/result
    _feedback = UP_DOWNFeedback()
    _result   = UP_DOWNResult()
    
    def __init__(self):
    # creates the action server
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
        self._as = actionlib.SimpleActionServer("/action_ex", UP_DOWNAction, self.goal_callback, False)
        self._as.start()
    
    def Twist_Write(self, Twist):
        self.TwistWrite = self.pub.publish(Twist)    
    
    def goal_callback(self, goal):
    # this callback is called when the action server is called.
    # this is the function that make the drone move
        Twist_value = Twist()
        
    
        if goal == "UP":
            Twist_value.linear.x  = 0.0
            Twist_value.linear.y  = 0.0
            Twist_value.linear.z  = 1.0
            Twist_value.angular.x = 0.0
            Twist_value.angular.y = 0.0
            Twist_value.angular.z = 0.0
            
            self._feedback.going_up = "GOING UP"
            
        if goal == "DOWN":
            Twist_value.linear.x  = 0.0
            Twist_value.linear.y  = 0.0
            Twist_value.linear.z  = -1.0
            Twist_value.angular.x = 0.0
            Twist_value.angular.y = 0.0
            Twist_value.angular.z = 0.0
            
            self._feedback.going_down = "GOING_DOWN"
            
        self.Twist_Write(Twist_Value)
        
        
        success = True  # if everithing was fine go on
   
        # at this point, either the goal has been achieved (success==true)
        # or the client preempted the goal (success==false)
        # If success, then we publish the final result
        # If not success, we do not publish anything in the result
        if success:
          self._result.SUCCESS = "SUCCES"
          #rospy.loginfo('Succeeded calculating the Fibonacci of order %i' % fibonacciOrder )
          self._as.set_succeeded(self._result)
      
if __name__ == '__main__':
  rospy.init_node('serverUPDOWN_node')
  UP_DOWNClass()
  rospy.spin()