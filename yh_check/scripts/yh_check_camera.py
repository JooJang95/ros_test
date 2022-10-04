#! /usr/bin/python3
#-*- coding: utf-8 -*-

import rospy
from yh_check.msg import YhCheck

def camera():
    rospy.init_node("yh_check_camera")
    my_pub_camera = rospy.Publisher("check_distance",YhCheck)
    
    loop_rate = rospy.Rate(2.5)

    msg = YhCheck()
    
    while not rospy.is_shutdown():
        msg.stamp = rospy.Time.now()
        my_pub_camera.publish(msg)
        loop_rate.sleep()

if __name__ == "__main__":
    camera()