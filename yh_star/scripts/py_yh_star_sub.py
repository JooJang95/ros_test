#! /usr/bin/python3
#-*- coding : utf-8 -*-

import rospy
from yh_star.msg import YhStarMsg

def msg_Callback(msg):
    n = msg.data    

    for i in range(1,n//2):
        for j in range(i):
            print("*",end='')
        print()    
    for i in range(n//2+1,n+1):
        for j in range(i):
            print("*",end='')
        print()

def subscriber_test2():
    rospy.init_node("yh_star_sub")
    sub = rospy.Subscriber("yh_star_topic",YhStarMsg,msg_Callback,queue_size=20)

    rospy.spin()

if __name__ == "__main__":
    subscriber_test2()