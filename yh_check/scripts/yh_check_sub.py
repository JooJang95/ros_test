    #! /usr/bin/python3
#-*- coding: utf-8 -*-

import rospy
from yh_check.msg import YhCheck

def check(msg):
    

def yh_check_sub():    
    rospy.init_node("yh_dual_time")
    
    sub = rospy.Subscriber("yh_dual_topic",100,check)
     
    rospy.spin()

if __name__ == "__main__":
    yh_check_sub()