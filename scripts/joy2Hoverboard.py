#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
 
# This ROS Node converts Joystick inputs from the joy node
# into commands for turtlesim or any other robot
 
# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Twist commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed
def callback(data):
    twistRear = Twist()
    twistFront = Twist()
    twistRear.linear.x = -2.5*data.axes[1]
    twistRear.angular.z = 1.5*data.axes[3]
    twistFront.linear.x = -2.5*data.axes[1]
    twistFront.angular.z = 1.5*data.axes[3]
    pubRear.publish(twistRear)
    pubFront.publish(twistFront)
 
# Intializes everything
def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    global pubRear,pubFront
    
    rospy.init_node('Joy2Hoverboard_node')
    pubRear = rospy.Publisher('/rear/hoverboard_velocity_controller/cmd_vel', Twist,queue_size=10)
    pubFront = rospy.Publisher('/front/hoverboard_velocity_controller/cmd_vel', Twist,queue_size=10)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    # starts the node
    rospy.spin()
 
if __name__ == '__main__':
    start()