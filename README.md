# ros_test
my_first_ros_study

### 22년 9월 27일 ROS 시작 (화요일)
- topic_tutorial 패키지 생성
- my_publisher, my_subscriber
노드 생성
-빌드
-실행

### 22년 9월 28일 (수요일) 

- py_publisher.py, py_subscriber.py 노드 생성
- topic_second 패키지 생성
- second_pub, second_sub, py_second_pub.py, py_second_sub.py 노드 생성
- 빌드
- 실행

- [과제 1번](./topic_test/)

### 22년 9월 29일 (목요일)

- [msg_tutorial](./msg_tutorial/)

   - msg_tutorial 패키지 생성
   - msg 디렉토리에 Mymsg.msg 생성
   - msg_publisher,msg_subscriber,
     py_msg_pub,py_msg_sub 생성
   - 빌드
   - 생성

- service_tutorial
   - service_tutorial 패키지 생성
   - srv 디렉토리에 AddTwoInts.srv 생성
   - my_client.cpp,my_server.cpp,
     py_client.py,py_server.py 노드 생성
   - 빌드
   - 실행

### 22년 9월 30일 (금요일)

- [과제2yh_star] (./yh_star)
  - yh_star 패키지 생성
  - yh_star_pub, yh_star_sub,
  yh_star_pub.py, yh_star_sub.py 노드생성
  - 빌드
  - 실행

- [과제3yh_service] (./yh_service)
  - yh_service 패키지 생성
  - yh_server, yh_client,
  yh_server.py, yh_client.py 노드생성
  - 빌드
  - 실행

### 22년 10월 4일 (화요일)
  - [param_tutorial](./param_tutorial/) 패키지 생성
  - param_tutorial 생성
  - calculate_server,calculate_client,
  calculate_server.py ,calculate_client.py 노드 생성
  -빌드 
  -실행 
  - [파라미터 서버 활용] (parameter-server)


## [과제4](./yh_dual/)

## [과제5](./yh_difference/)

### 22년 10월 5일 (수요일)

## [과제6](./yh_check/)
  - yh_check 패키지 생성
  - yh_check_distance, yh_check_camera, yh_check_sub,
    yh_check_distance.py, yh_check_camera.py,
    yh_check_sub.py  노드생성
  - 빌드
  - 실행
  - python class로 작성

## [과제7](./yh_connect/)
  - yh_check 패키지 생성
  - yh_connect_pub, yh_connect_sub_pub, yh_connect_sub,
    yh_connect_pub.py, yh_connect_sub_pub.py, 
    yh_connect_sub.py  노드생성
  - 빌드
  - 실행
  - python class로 작성

### 22년 10월 6일 (목요일)
## [yh_turtle](./yh_turtle/)
 - yh_turtle 패키지 생성
 - turtle_clear, turtle_keyboard_clear, turtle_keyboard, turtle_patrol
   turtle_clear.py, turtle_keyboard_clear.py, turtle_keyboard.py, turtle_patrol.py
 - 빌드
 - 실행
 - python class로 작성

 ### 22년 10월 7일 (금요일)
 - turtle_circle.py turtle_triangle.py turtle_goal.py 노드생성
 - turtle_goal에서 인공지능 구현
 - 빌드
 - 실행

### [roslaunch](./yh_turtle/launch/)
  - roscore와 launch 파일에 있는 노드들을 실행시키는 명령
  - launch 파일은 '패키지 디렉토리/launch'에 만든다.
  - roslaunch 실행
  
  '''bash
  $ roslaunch <패키지이름> <런치파일이름>

  '''

  - launch 파일은 <launch></launch>태그 사이에 내용을 입력한다.
  - node 태그는 패키지 이름, 노드 타입 ,노드 이름을 입력한다.
  - param 태그는 파라미터 이름, 값, 타입을 입력한다.

### 22년 10월 7일 (금요일)
 - turtle_circle.py turtle_triangle.py turtle_goal.py 노드생성
 - turtle_goal

 





### teleop_twist_keyboard
 - 키보드 입력을 받아 /cmd_vel 토픽의 geometry_msgs/Twist
 메시지로 publish하는 노드
 - 설치
 '''bash
 $ sudo apt install ros-melodic


### ROS 명령어
```- roscore 마스터 실행 명령어
- rosrun <패키지이름> <실행파일이름> 노드 실행 명령어
- rqt_graph  노드들의 정보를 그림으로 볼수있는 명령어
```

### catkin_create_pkg
- 현재 위치한 작업 공간에 패키지를 생성한다.
- catkin_create_pkg <패키지 이름> <의존성>
``` bash
        catkin_create_pkg <패키지이름> <의존성 1> <의존성 2>.... 띄어쓰기로 구분
```
``` bash
        catkin_create_pkg
        예시 :
        패키지이름 : topic_tutorial
        의존성 : roscpp rospy std_msgs
```
### parameter-server
  - ROS Master에서 실행되고, 변수들을 담
  있는 서버
  - ros::setParam(), ros::getParam(),
  rospy.set_param(), rospy.get_param() 등의 함수로 사용
  - command lien에서 rosparam으로 사용 가능 
  - rosparam list
    - 파라미터 서버의 모든 파라미터를 출력
  '''bash
  joojang@ubuntu:~$ rosparam get <파라미터 이름>
  '''

  - rosparam set <파라미터 이름> [파라미터 값]
    - 파라미터의 값을 지정함
  '''bash
  joojang@ubuntu:~$ rosparam set <파라미터 이름> [파라미터 값]
  '''
