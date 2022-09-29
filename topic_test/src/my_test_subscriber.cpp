#include "ros/ros.h"
#include "std_msgs/Int64.h"

void test_msg_Callback(const std_msgs::Int64::ConstPtr& msg){
    ROS_INFO("msg : %d",msg->data);
}

int main(int argc,char** argv){

    ros::init(argc,argv,"my_test_subscriber");
    ros::NodeHandle nh;

    ros::Subscriber sub = nh.subscribe("my_test_listener",100,test_msg_Callback);

    ros::spin();
    
}