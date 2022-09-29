#include "ros/ros.h"
#include "msg_tutorial/Mymsg.h" //Mymsg 메시지 헤더 파일
                                //빌드시 자동 생성

int main(int argc,char** argv){

    ros::init(argc,argv,"msg_publisher"); // init 선언 (argc,argv,노드이름)
    ros::NodeHandle nh;                  // ros::NodeHandle nh 선언

    ros::Publisher pub = nh.advertise<msg_tutorial::Mymsg>("burger",20); 
    //ros::Publisher 자료형 pub 변수를 만들고 nh.advertise 에 <메시지타입> ("토픽이름",큐사이즈)

    ros::Rate loop_rate(2);
    //ros::Rate 자료형 loop_rate 정의

    msg_tutorial::Mymsg msg;
    int cnt =0;
    // msg_tutorial::Mymsg 자료형 msg 선언
    // 정수형 cnt 카운트 선언


    while(ros::ok()){

        msg.stamp = ros::Time::now(); // 현재 시간을 msg의 stamp에 담는다.        
        msg.data = cnt;               // cnt 변수의 값으 msg의 data에 담는다.
        ROS_INFO("send msg : %d",msg.stamp.sec); //stamp.sec를 출력한다.   (seconds)
        ROS_INFO("send msg : %d",msg.stamp.nsec); //stamp.nsec를 축력한다. (nanoseconds)
        ROS_INFO("send msg : %d",msg.data); // data를 출력한다.
        pub.publish(msg);  
        cnt++;
        loop_rate.sleep();
    }


    return 0;
}
