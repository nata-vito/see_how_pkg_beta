#!/usr/bin/env python2

import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

cap = cv2.VideoCapture(0)

# Verifying the camera input 
print(cap.isOpened())

# CvBridge to work with ROS
bridge = CvBridge()


def talker():
    pub = rospy.Publisher('/camera', Image, queue_size = 1)
    rospy.init_node('image', anonymous=True)
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        
        while True:
            ret, frame = cap.read()
            
            if not ret:
                break
            
            msg = bridge.cv2_to_imgmsg(frame, "bgr8")
            pub.publish(msg)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            if rospy.is_shutdown():
                cap.release()
                
if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass