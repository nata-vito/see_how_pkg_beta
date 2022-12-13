#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

class Publisher:
    def __init__(self, mpHands = None, hands = None, mpDraw = None, handFingers = None, 
                 fingers = None, side = None, countFingers = None, nodeName = None):

        self.mpHands            = mpHands
        self.hands              = hands
        self.mpDraw             = mpDraw
        self.handFingers        = handFingers
        self.fingers            = fingers
        self.side               = side
        self.countFingers       = countFingers
        self.nodeName           = nodeName

    def talker(self):
        pub = rospy.Publisher(self.nodeName, String, queue_size=10)
        rospy.init_node('left_hand', anonymous=True)
        rate = rospy.Rate(100)
        rate.sleep()

    
        hello_str = "Hello World %s" % rospy.get_time()
        pub.publish(hello_str)
        #rate.sleep()


