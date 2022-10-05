#! /usr/bin/python
#-*- coding: utf-8 -*- 

import rospy
from yh_check.msg import YhCheck 

msg_camera = YhCheck() 

def yh_check_camera():
    rospy.init_node("yh_check_camera")    

    pub = rospy.Publisher("check_camera",YhCheck,queue_size= 100) 

    loop_rate = rospy.Rate(2.5)    
    msg = YhCheck()
    
    msg.data = True # bool 자료형 변수 초기화

    while not rospy.is_shutdown():        
        msg.stamp = rospy.Time.now()
        if (msg.data == True): msg.data = False
        else : msg.data = True
        pub.publish(msg)
        loop_rate.sleep()

if __name__ == "__main__":
        yh_check_camera()   