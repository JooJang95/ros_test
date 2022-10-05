#! /usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
from yh_connect.msg import YhCon

def yh_connect_pub():
    rospy.init_node("yh_connect_pub")
    pub = rospy.Publisher("yh_connect_sub_pub",YhCon,queue_size=100)
    
    msg = YhCon()
    msg.int = 0        #초기화    
    loop_rate = rospy.Rate (4)

    while not rospy.is_shutdown():
        pub.publish(msg)
        rospy.loginfo("%d",msg.int)
        msg.int += 1        
        loop_rate.sleep()

if __name__ == "__main__":
    yh_connect_pub()