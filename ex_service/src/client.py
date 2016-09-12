#! /usr/bin/env python

import rospy
import rospkg
import sys 

from iri_wam_reproduce_trajectory.srv import ExecTraj # import the service message used by the service /gazebo/delete_model


rospy.init_node('client_node') # initialise a ROS node with the name service_client

rospy.loginfo('waiting service')

rospy.wait_for_service('/execute_trajectory') # wait for the service client /gazebo/delete_model to be running

rospy.loginfo('finish wait service')

execute_trajectory_service = rospy.ServiceProxy('/execute_trajectory', ExecTraj) # create the connection to the service

rospack = rospkg.RosPack()

traj = ExecTraj()         # This rospack.get_path() works in the same way as $(find name_of_package) in the launch files.

traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"
result = execute_trajectory_service(traj) # send through the connection the name of the object to be deleted by the service
rospy.loginfo('Success') # print the result given by the service calledSettings