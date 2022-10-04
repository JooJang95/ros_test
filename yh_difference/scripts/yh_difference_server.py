#! /usr/bin/python3
#-*- coding: utf-8 -*-

import rospy
from yh_difference.srv import YhDifference,YhDifferenceResponse

def Calculation(req):
    res = YhDifferenceResponse()
    if req.a > req.b :
        result = req.a - req.b
    elif req.a < req.b : 
        result = req.b - req.a
    res.result = result
    rospy.loginfo(f"a: {req.a}, b: {req.b}, result: {res.result}")        
    return res
def yh_difference_server():
    rospy.init_node("yh_difference_server")
    my_server = rospy.Service("difference",YhDifference,Calculation)

    rospy.loginfo("Service Server Ready")

    rospy.spin()

if __name__ == "__main__":
    yh_difference_server()


