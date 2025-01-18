# -*- encoding: UTF-8 -*-
from __future__ import print_function
import socket
import math
import time
import threading
from contextlib import closing
from naoqi import ALProxy

# Wireless
#ROBOT_IP = '192.168.253.12'
#Local Connection
ROBOT_IP = "169.254.168.203"
ROBOT_PORT = 9559
#Parameters taken from walkmate
miu = 3.2
K = 5

theta_m = 0
omega_m = 2 * math.pi
delta_t = 0.02  #20ms
action_flag = 0

#Timer
class TimerSet(threading.Thread):
    def run(self):
        global action_flag
        if action_flag == 1:
            time.sleep(5)
            action_flag = 0
        print ("Exiting Thread")
        #Preparation for restarting thread
        self.__init__()

#Robot Part
class Actuator(threading.Thread):
    def run(self):
        motion = ALProxy ('ALMotion', ROBOT_IP, ROBOT_PORT)

        motion.setStiffnesses ('Head', 1.0)

        global theta_m

        while 1:
            while theta_m < 2 * math.pi:
                theta_m += (omega_m + K * math.sin(-theta_m)) * delta_t
                #print('Robot phase: {0}!'.format(str(theta_m)))
                time.sleep(0.02)

            theta_m = 0
            if action_flag == 1:
                print('Pong!')
                try:
                    motion.post.angleInterpolation (
                        ['HeadPitch'],
                        [0.0, 0.1, 0.0],
                        [0.001, 0.1, 0.2],
                        False
                    )
                    time.sleep(0.2)
                except BaseException, err:
                    print(err)


#Human part
class Controller(threading.Thread):
    def run(self):
        host = 'localhost'
        port = 10000
        buffersize = 4096
        norm_queue = list()
        global omega_m
        global action_flag
        nod_flag = 0

        timerset = TimerSet()
        #total_theta_h = 0
        #total_period_T = 0
        #starting phase changing velocity
        #omega_h = 0

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        with closing(sock):
            sock.connect((host, port))
            while 1:
                #theta_h = 0
                #period_T = 0

                buffstr = sock.recv(buffersize).replace('\x00', '')
                bufflist = buffstr.split(',')

                #time = float(bufflist[1])

                #Get angular_velocity_h
                angular_velocity_h = float(bufflist[6])

                while angular_velocity_h > 1000:
                    #if total_period_T != 0:
                    nod_flag = 1
                        #theta_h += omega_h * delta_t
                        #if theta_h >= 2 * math.pi:
                        #    theta_h = 0

                    buffstr = sock.recv(buffersize).replace('\x00', '')
                    bufflist = buffstr.split(',')

                    #Get angular_velocity_h
                    angular_velocity_h = float(bufflist[6])

                if nod_flag == 1:
                    omega_m -= miu * math.sin(-theta_m) * delta_t
                    #print(omega_m)
                    print('Ping! Robot phase changing v: {0}'.format(str(theta_m)))
                    try:
                        if not timerset.is_alive():
                            timerset.run()
                            action_flag = 1
                    except BaseException, err:
                        print(err)

                nod_flag = 0


def main():
    actuator = Actuator()
    controller = Controller()
    actuator.start()
    controller.start()

if __name__ == '__main__':
    main()
