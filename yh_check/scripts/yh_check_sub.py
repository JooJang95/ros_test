#! /usr/bin/python
#-*- coding: utf-8 -*- 

import rospy
from yh_check.msg import YhCheck 


Bool_distance = True
Bool_camera = True

def sub_Collback_distance(msg):
    global Bool_distance
    Bool_distance = msg.data
    rospy.loginfo("distance : %d",Bool_distance)
    if Bool_camera and Bool_distance == True:
        rospy.loginfo("----------OK----------")

def sub_Collback_camera(msg):
    global Bool_camera
    Bool_camera = msg.data  
    rospy.loginfo("camera : %d",Bool_camera)
    if Bool_camera and Bool_distance == True:
        rospy.loginfo("----------OK----------")
    
def yh_check_sub():
    rospy.init_node("py_check_sub")   

    
    sub_distance = rospy.Subscriber("check_distance",YhCheck,sub_Collback_distance)
    sub_camera = rospy.Subscriber("check_camera",YhCheck,sub_Collback_camera)

    rospy.spin() 

if __name__ == "__main__":
    yh_check_sub()
