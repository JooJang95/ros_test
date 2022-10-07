#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
#include "turtlesim/TeleportAbsolute.h"

ros::Publisher pub;
ros::ServiceClient circle_client;
turtlesim::TeleportAbsolute srv;
float R = 10;
float pie = 3.14;

void msgCallback(const geometry_msgs::Twist::ConstPtr& msg){
    pub.publish(*msg);
    if(msg -> linear.z > 0.0){        
        srv.request.x = 5.5;
        srv.request.y = R;
        srv.request.theta = 0.0;
                       
        if(circle_client.call(srv)){                      
            ROS_INFO("CLEAR");
        }
        else{
            ROS_INFO("FAILED");
        }
    }
}

int main (int argc,char** argv){
    ros::init(argc,argv,"turtle_keyboard_clear");
    ros::NodeHandle nh;

    pub = nh.advertise<geometry_msgs::Twist>("turtle1/cmd_vel",100);
    circle_client = nh.serviceClient<turtlesim::TeleportAbsolute>("turtle1/teleport_absolute",100);
    ros::Subscriber sub = nh.subscribe("cmd_vel",100,msgCallback);

    ros::spin();

    return 0;
}