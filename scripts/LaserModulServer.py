import rospy
import actionlib
from bark_msgs.msg import LaserModulAction
from time import sleep
import RPi.GPIO as GPIO

class LaserModul:
    def __init__(self):
        # pin 3 => BCM 2
        self.GPIO_name = 2
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.GPIO_name,GPIO.OUT)
        GPIO.output(self.GPIO_name,1)

        self.server = actionlib.SimpleActionServer('laser_modul', LaserModulAction, self.execute, False)
        self.server.start()
        sleep(0.5)

    def on(self):
        GPIO.output(self.GPIO_name,0)

    def off(self):
        GPIO.output(self.GPIO_name,1)

    def execute(self, goal):
        if goal.on:
            self.on()
        else:
            self.off()

        # empty respons
        self.server.set_succeeded()


if __name__ == '__main__':
    rospy.init_node('laser_modul_server')

    server = LaserModul()
    rospy.spin()