#! /usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
from yh_connect.msg import YhCon

def yh_Callback(msg):
    rospy.loginfo("result : %lf ", msg)
   

def yh_connect_sub():
    rospy.init_node("yh_connect_sub")
    
    rospy.Subscriber("yh_connect_sub",YhCon,yh_Callback)

    rospy.spin()

if __name__ == "__main__":
    yh_connect_sub()
        
        