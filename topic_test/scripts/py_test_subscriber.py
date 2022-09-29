#! /usr/bin/python
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int64

def test_Callback(msg):
    rospy.loginfo("msg : %d ",msg.data)
    

def test_listener():
    rospy.init_node("py_test_subscriber")
    rospy.Subscriber("topic_test",Int64,test_Callback,queue_size=100)

    rospy.spin()

if __name__ == "__main__":
    test_listener()
