#include "ros/ros.h"
#include "std_msgs/Int64.h"

int main(int argc,char** argv){

    ros::init("__test_publisher");
    ros::NodeHandle nh;

    ros.Publisherpub = nh.advertise<std_msgs::Int64>("my_test_count",100);
    ros::Rate loop_rate(4);

    std_msgs::Int64 msg;
    msg.data = 0;
    
    while(ros::ok()){
        ROS_INFO(msg);
        loop_rate.sleep();
        msg.data++;
        if (msg.data > 100){
            msg.data = 0;
        }
    }

    return 0;    
}