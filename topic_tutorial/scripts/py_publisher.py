#!/usr/bin/python
#-*- coding: utf-8 -*-

from asyncore import loop
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher("my_topic", String, queue_size=100)
    rospy.init_node("py_pyblisher")
    
    loop_rate = rospy.Rate(10)

    msg = String()
    msg.data = "Hi"

    while not rospy.is_shutdown():
        pub.publish(msg)
        loop_rate.sleep()

if __name__ == "__main__":
    talker()