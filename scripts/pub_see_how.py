#!/usr/bin/env python3
import rospy
import geometry_msgs.msg
from std_msgs.msg import String

class Publisher:
    def __init__(self, fingers = None, side = None, countFingers = None, nodeName = None):
        
        rospy.init_node('left_hand', anonymous=True)
        self.fingers            = fingers
        self.side               = side
        self.countFingers       = countFingers
        self.nodeName           = nodeName
        self.timestamp          = rospy.get_time()
        self.pub = rospy.Publisher(self.nodeName, String, queue_size=10)

    def talker(self):
        rate = rospy.Rate(100)
        rate.sleep()
            
        data = "Timestamp: " + str(self.timestamp) + "\n" + "Side: " + str(self.side) + "\n" 
        self.pub.publish(data)
        #rate.sleep()


