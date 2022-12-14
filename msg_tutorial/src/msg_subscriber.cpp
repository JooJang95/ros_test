#include "ros/ros.h"
#include "msg_tutorial/Mymsg.h" //Mymsg 메시지 헤더 파일
                                //빌드시 자동 생성
//void msgCallback(const std_msgs::Int64::cosntPtr& msg)
void msgCallback(const msg_tutorial::Mymsg::ConstPtr& msg){
    ROS_INFO("receive msg : %d", msg->stamp.sec);   //msg의 stamp의 sec을 출력한다.   (second)
    ROS_INFO("receive msg : %d", msg->stamp.nsec);  //msg의 stamp의 nsec을 출력한다.  (nanosecond)
    ROS_INFO("receive msg : %d", msg->data);        //msg의 stamp의 data을 출력한다.  (data)
}

int main(int argc,char** argv){
    
    ros::init(argc,argv,"msg_subscriber");
    ros::NodeHandle nh;

    ros::Subscriber sub = nh.subscribe("burger", 30, msgCallback);

    ros::spin();

    return 0;
}