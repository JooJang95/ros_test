#include "ros/ros.h"
#include "std_msgs/Int32.h"

int main(int argc,char** argv){

    ros::init(argc,argv,"yh_connect_pub");
    ros::NodeHandle nh;
    
    ros::Publisher pub = nh.advertise<std_msgs::Int32>("yh_connect_pub",10);

    ros::Rate loop_rate(4);

    return 0;
}