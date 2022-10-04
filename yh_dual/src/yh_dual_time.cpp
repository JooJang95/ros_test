#include "ros/ros.h"
#include "yh_dual/YhDual.h"

void time_Collback(const yh_dual::YhDual::ConstPtr& msg){
    ROS_INFO("%d,%d",msg->stamp.sec,msg->stamp.nsec);    
}

int main(int argc,char** argv){
    ros::init(argc,argv,"yh_dual_time");   
    
    ros::NodeHandle nh;

    ros::Subscriber sub_int =  nh.subscribe("yh_dual_topic",100,time_Collback);
     
    ros::spin();

    return 0;
}