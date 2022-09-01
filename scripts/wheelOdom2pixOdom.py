#! /usr/bin/env python
from re import sub
import rospy
from std_msgs.msg import UInt16MultiArray
from geometry_msgs.msg import Twist
from mavros_msgs.msg import RCOut
from nav_msgs.msg import Odometry


odomMsg=Odometry()
twistRear=Twist();twistFront=Twist()

pubMavrosOdom=rospy.Publisher("/mavros/odometry/in",Odometry,queue_size=10)  

def rcOut_callback(msg):
    print("data  steer: ",msg.channels[0])
    print("data  steer: ",msg.channels[2])
    if msg.channels[2]>1600:
        twistRear.angular.z=-0.25
        twistFront.angular.z=0.25
    elif msg.channels[2]<1500:
        pass
    
def subFrontOdom_cb(msg):
    odomMsg.header.frame_id="map"
    odomMsg.child_frame_id="base_link"
    odomMsg.twist=msg.twist
    odomMsg.pose=msg.pose
    
    pubMavrosOdom.publish(odomMsg)
    
def main():
    
    rospy.init_node("wheelOdom2pixOdom_node")
    
      
    # subRearOdom=rospy.Subscriber("/rear/hoverboard_velocity_controller/odom",Odometry,queue_size=10)
    subFrontOdom=rospy.Subscriber("/front/hoverboard_velocity_controller/odom",Odometry,subFrontOdom_cb)
    subFrontOdom_cb(odomMsg)
    rospy.spin()

if __name__ == '__main__':
    main()
    