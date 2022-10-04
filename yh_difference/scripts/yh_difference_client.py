#! /usr/bin/python3
#-*- coding: utf-8 -*-

import rospy
from yh_difference.srv import YhDifference,YhDifferenceRequest
import sys


def yh_difference_client():
    rospy.init_node("yh_difference_client")
    
    if len(sys.argv) != 3:
        rospy.loginfo("rosrun yh_service yh_client.py a b")
        rospy.loginfo("a, b: int32 number")
        sys.exit(1)
    
    my_client = rospy.ServiceProxy("difference",YhDifference)
    req = YhDifferenceRequest()
    req.a = int(sys.argv[1])
    req.b = int(sys.argv[2])

    try:
        res = my_client(req)
        rospy.loginfo(f"a:{req.a}, b:{req.b}, result:{res.result}")
    except rospy.ServiceException as e:
        rospy.loginfo(f"Failde: {e}")
        sys.exit(1)

if __name__ == "__main__":
    yh_difference_client()