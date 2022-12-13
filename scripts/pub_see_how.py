#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

class Publisher:
    def __init__(self, mpHands = None, hands = None, mpDraw = None, handFingers = None, 
                 fingers = None, side = None, countFingers = None):

        self.mpHands            = mpHands
        self.hands              = hands
        self.mpDraw             = mpDraw
        self.handFingers        = handFingers
        self.fingers            = fingers
        self.side               = side
        self.countFingers       = countFingers

    def talker(self):
        pub = rospy.Publisher('chatter', String, queue_size=10)
        rospy.init_node('talker', anonymous=True)
        rate = rospy.Rate(10)

        while not rospy.is_shutdown():
            hello_str = "Hello World %s" % rospy.get_time()
            pub.publish(hello_str)
            rate.sleep()
    
    def runTopic(self):
        if __name__ == '__main__':
            try:
                self.talker()
            except rospy.ROSInterruptException:
                pass

pub = Publisher()
pub.runTopic()