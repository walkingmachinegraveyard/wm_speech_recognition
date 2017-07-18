#!/usr/bin/env python
import rospy
import roslib

import time

from std_msgs.msg import String

import speech_recognition as sr

def speech():
    r = sr.Recognizer()

    pub = rospy.Publisher("speech", String, queue_size=1)
    rospy.init_node('speech_recognition')

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) # listen for 1 second to calibrate
        while not rospy.is_shutdown():
            audio = r.listen(source)
            try:
                pub.publish(r.recognize_google(audio))
            except:
                pass
            time.sleep(4)

if __name__ == '__main__':
    try:
        speech()
    except rospy.ROSInterruptException:
        pass
