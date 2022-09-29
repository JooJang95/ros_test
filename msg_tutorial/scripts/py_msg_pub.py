#! /usr/bin/python
#-*- coding: utf-8 -*-

import rospy                         # rospy import 가져옴
from msg_tutorial.msg import Mymsg   # 미리 정의해논 msg파일을 가져옴

def msg_talker():
    rospy.init_node("py_msg_pub") # 노드이름 

    pub = rospy.Publisher("burger", Mymsg, queue_size=10)
    # publisher 생성 ("topic name",massage type, queue size)

    loop_rate = rospy.Rate(5)
    #Rate 0.2초로 생성 및 설정

    msg = Mymsg()
    # msg생성 및 대입 
    cnt = 0

    while not rospy.is_shutdown():     # 반복문 ( C++ 에서 ros::ok()랑 같은 역할 )
        msg.stamp = rospy.Time.now()   # rospy.Time.now() 현재시간 
        msg.data = cnt                 # 카운트를 세기위해 msg.data에 cnt 대입
        rospy.loginfo("send msg : %d", msg.stamp.secs)     # 출력함수
        rospy.loginfo("send msg : %d", msg.stamp.nsecs)
        rospy.loginfo("send msg : %d", msg.data)
        pub.publish(msg)               # msg를 ublisher
        loop_rate.sleep()              # 위에 정의한 Rate 간격
        cnt += 1                       # 반복문을 돌면서 카운트에 1씩 더해준다.

if __name__ == "__main__":             #if __name__ == "__main__" : 이 함수의 재사용성 및 이 파일에서만 실행 시키기 위해 넣음.
    try:
        msg_talker()
    except rospy.ROSInterruptException:
        pass
