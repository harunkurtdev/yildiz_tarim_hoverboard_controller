#include "ros/ros.h"
#include <geometry_msgs/Twist.h>
#include <std_msgs/UInt16MultiArray.h>

#include <mavros_msgs/RCOut.h>

ros::Publisher pub_rearWheel;
ros::Publisher pub_frontWheel;
geometry_msgs::Twist rear_msg;
geometry_msgs::Twist front_msg;
mavros_msgs::RCOut rcOut;
std_msgs::UInt16MultiArray val_rcOut;
// void rear_wheel_callBack(const geometry_msgs::Twist &msg){
//     rear_msg.linear.x=msg.linear.x;
//     rear_msg.angular.z=-msg.angular.z;
//     pub_rearWheel.publish(rear_msg);
// }

// void front_wheel_callBack(const geometry_msgs::Twist &msg){
//     front_msg.linear.x=msg.linear.x;
//     front_msg.angular.z=msg.angular.z;
//     pub_frontWheel.publish(front_msg);
// }


// void rcOut_callBack(const mavros_msgs::RCOut::ConstPtr& msg){
    
//     rcOut=*msg;
//     val_rcOut.data=rcOut.channels;
//     ROS_INFO("%d",val_rcOut.data[0]);
//     // front_msg.linear.x=msg.linear.x;
//     // front_msg.angular.z=msg.angular.z;
//     // pub_frontWheel.publish(front_msg);
// }

mavros_msgs::RCOut current_rcout;
void rcout_cb(const mavros_msgs::RCOut::ConstPtr& msg)
{
    current_rcout = *msg;
}

int main(int argc, char **argv)
{
    ros::init(argc,argv,"hoverboard_controller_node");
    // ros::init(argc,argv,"hoverboard_controller_node");
    ros::NodeHandle n;
    

    // ros::Subscriber rear_sub=n.subscribe("/cmd_vel",10,rear_wheel_callBack);
    // ros::Subscriber front_sub=n.subscribe("/cmd_vel",10,front_wheel_callBack);
     ros::Subscriber rcout_sub = n.subscribe<mavros_msgs::RCOut>("mavros/rc/out", 50, rcout_cb);

    // ros::Subscriber mavros_RCOut_sub=n.subscribe<mavros_msgs::RCOut>("/mavros/rc/out",10,rcOut_callBack);
    pub_rearWheel=n.advertise<geometry_msgs::Twist>("/rear/hoverboard_velocity_controller/cmd_vel",10);
    pub_frontWheel=n.advertise<geometry_msgs::Twist>("/front/hoverboard_velocity_controller/cmd_vel",10);
    return 0;
}
