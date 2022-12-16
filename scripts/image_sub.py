#!/usr/bin/env python2
import sys
import rospy
import cv2 as cv
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
#import hand_tracking as ht

class image_converter:
    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("camera", Image, self.image_callback)
        self.img = None

    def image_callback(self, msg):
        try:
            self.img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
            print(self.img)
            self.showImage()
        except CvBridgeError as e:
            rospy.logerr("CvBridge Error: {0}".format(e))
            
        
    
    def showImage(self):
        if self.img is None:
            print("Could not read the image.")
        else:       
            cv.imshow("testing image", self.img)
            cv.waitKey(0)
        
       
        
        
def main(args):
    ic = image_converter()
    rospy.init_node('image_converter', anonymous=True)
    
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    
    cv.destroyAllWindows()
    
if __name__ == "__main__":
    main(sys.argv)