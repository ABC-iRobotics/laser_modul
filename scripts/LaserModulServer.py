import serial
from time import sleep
import rospy
import actionlib
from bark_msgs.msg import LaserModulAction

class LaserModul:

    def __init__(self):
        self.on = False
        self.angle = 0
        self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        self.server = actionlib.SimpleActionServer('laser_modul', LaserModulAction, self.execute, False)
        self.server.start()
        sleep(5)

    def execute(self, goal):
        # modul is already on, do the thing
        if goal.on and self.on:
            msg = 'MA:0,' + str(goal.angle) + ' /n'
            self.ser.write(msg.encode('utf-8'))
            self.angle = goal.angle
            sleep(2)
        
        # turn off the modul
        if ~goal.on and self.on:
            msg = 'LA:0'+ ' /n'
            self.ser.write(msg.encode('utf-8'))
            self.on = False
            sleep(2)
        
        # turn on and rotate
        if goal.on and ~self.on:
            msg = 'LA:1'+ ' /n'
            self.ser.write(msg.encode('utf-8'))
            self.on = True
            sleep(3)

            msg = 'MA:0,' + str(goal.angle) + ' /n'
            self.ser.write(msg.encode('utf-8'))
            self.angle = goal.angle
            sleep(2)

        # empty respons
        self.server.set_succeeded()


if __name__ == '__main__':
    rospy.init_node('laser_modul_server')

    server = LaserModul()
    rospy.spin()