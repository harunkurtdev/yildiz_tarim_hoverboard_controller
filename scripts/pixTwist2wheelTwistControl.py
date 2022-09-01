#! /usr/bin/env python

import rospy
from std_msgs.msg import UInt16MultiArray
from geometry_msgs.msg import Twist,TwistStamped
from mavros_msgs.msg import RCOut
from nav_msgs.msg import Odometry

rcOut=RCOut()
twistStamped=TwistStamped()

pubRear=rospy.Publisher("/rear/hoverboard_velocity_controller/cmd_vel",Twist,queue_size=10)
pubFront=rospy.Publisher("/front/hoverboard_velocity_controller/cmd_vel",Twist,queue_size=10)

twistRear=Twist();twistFront=Twist()

def mapPWM(x,in_min,in_max,out_min,out_max) : 
    return (x - in_min) * (out_max - out_min)/(in_max - in_min) + out_min

def rcOut_callback(msg):
    global z
    # z=0
    # print("data  steer: ",msg.channels[0])
    # print("data  steer: ",msg.channels[2])
    print("value throtlee",mapPWM(msg.channels[1],1100,1900,-1,1))
    print("value steering",mapPWM(msg.channels[0],1100,1900,-1,1)," print zz",-z)

    twistRear.linear.x=mapPWM(msg.channels[1],1100,1900,-0.5,0.5)
    twistFront.linear.x=mapPWM(msg.channels[1],1100,1900,-0.5,0.5)
    twistFront.angular.z=-(mapPWM(msg.channels[0],1100,1900,-1.5,1.5) -z)
    twistRear.angular.z=-(mapPWM(msg.channels[0],1100,1900,-1.5,1.5) -z)
    
    pubFront.publish(twistFront);pubRear.publish(twistRear)    
    

def twistStamped_callback(msg):
    
    twistRear.linear.x=msg.twist.linear.x
    twistFront.linear.x=msg.twist.linear.x
    twistFront.angular.z=msg.twist.angular.z
    twistRear.angular.z=msg.twist.angular.z
    
    pubFront.publish(twistFront);pubRear.publish(twistRear)    

def scan_callback(msg):
    global z
    z=msg.angular.z
    # print("print zz", z)
    
    
    
    
def main():
    
    
    rospy.init_node("pixTwist2wheelTwistControl_node")
    
    
    subRCOut=rospy.Subscriber("/mavros/rc/out",RCOut,rcOut_callback)    
    subRCOut=rospy.Subscriber("/scan/cmd_vel",Twist,scan_callback)    
    # subRCOut=rospy.Subscriber("/mavros/local_position/velocity_body",TwistStamped,twistStamped_callback)
    
    rospy.spin()

if __name__ == '__main__':
    z=0
    main()
    