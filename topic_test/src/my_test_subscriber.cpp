#include "ros/ros.h"
#include "std_msgs/Int64.h"

void test_msg_Callback(const std_msgs::Int64::constPtr& msg){
    ROS_INFO("msg : %d",msg -> data);
}

int main(int argc,char** argv){

    ros::init("__test_subscriber");
    ros::NodeHandle nh;

    ros.subscriber sub = nh.Subscribe("my_test_listener",test_msg_Callback,100);
}