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
            if not rospy.get_param("offline"):
                try:
                    data = r.recognize_google(audio)
                    pub.publish(data)
                except:
                    rospy.logwarn("No word detected")
                time.sleep(2)

            if rospy.get_param("offline"):
                try:
                    pub.publish(r.recognize_sphinx(audio))
                except:
                    rospy.logwarn("No word detected")
                time.sleep(2)

if __name__ == '__main__':
    try:
        speech()
    except rospy.ROSInterruptException:
        pass
