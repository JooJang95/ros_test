# ros_test
my_first_ros_study

### 22년 9월 27일 ROS 시작 (화요일)
- topic_tutorial 패키지 생성
- my_publisher, my_subscriber
노드 생성
-빌드
-실행

### 22년 9월 28일 (수요일) 
- py_publisher.py, py_subscriber.py
노드 생성
-빌드
-실행


### ROS 명령어
```- roscore *마스터 실행 명령어*
- rosrun <패키지이름> <실행파일이름> *노드 실행 명령어*
- rqt_graph  *노드들의 정보를 그림으로 볼수있는 명령어*
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