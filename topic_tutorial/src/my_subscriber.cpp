#include "ros/ros.h" //ros 헤더파일
#include "std_msgs/String.h" //std_msgs 패키지의 String 메세지 헤더파일

void msgCallback(const std_msgs::String::ConstPtr& msg){
    ROS_INFO("msg : %s", msg->data.c_str());
}

int main(int argc,char** argv){
    
    ros::init(argc,argv,"my_subscriber"); // 노드 이름 초기화
    ros::NodeHandle nh; // 노드 핸들 선언 (노드들을 통신)

    //서브스크라이버 선언
    //패키지(std_msgs)의 메시지(String)를 이용한 서브스크라이버(sub)를 선언한다.    
    //토픽은 ( "my_topic" )이며, 서브스크라이버 큐(queue) 사이즈를 100으로 설정한다.
    // 콜백 함수는 (msgCallback)이다.
    ros::Subscriber sub = nh.subscribe("my_topic" ,100 , msgCallback);

    //콜백 함수 호출을 위한 함수, 메시지가 수신되기를 대기
    //수신되었을 경우 콜백 함수를 호출한다.
    ros::spin(); // 콜백 함수가 올때까지 대기


    return 0;
}