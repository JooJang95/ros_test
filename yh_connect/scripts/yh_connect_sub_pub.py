#! /usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
from yh_connect.msg import YhCon

def yh_claculate(msg):
    n = msg.int 
    m = msg.duoble
    if n % 5 == 0 :
        m = n /3
        msg.duoble = m
    #pub.publish(msg)        
    #rospy.loginfo("정수 : %d, 실수 : %lf",msg.int,msg.duoble)                
    #loop_rate.sleep(4)

    #rospy.loginfo("%d,%lf",msg.int,msg.duoble)


def yh_connect_sub_pub():
    rospy.init_node("yh_connect_sub_pub")    

    rospy.Subscriber("yh_connect_sub_pub",YhCon,yh_claculate)

    pub = rospy.Publisher("yh_connect_sub",YhCon,queue_size=100)

    loop_rate = rospy.Rate(4)

    rospy.spin()


if __name__ == "__main__":
    try:
        yh_connect_sub_pub()
    except rospy.ROSInternalException:
        pass
    