# -*- encoding: UTF-8 -*-
from __future__ import print_function
import socket
import math
import time
import threading
import random
from contextlib import closing
from naoqi import ALProxy

#Wireless
#ROBOT_IP = '192.168.253.39'
#Local Connection
ROBOT_IP = "169.254.168.203"
ROBOT_PORT = 9559
#nod counter, random int 3~6
counter = 15

def answer1():
    tts = ALProxy("ALTextToSpeech", ROBOT_IP, ROBOT_PORT)
    tts.setLanguage("Japanese")
    tts.setParameter("speed", 1.0)
    tts.say("はい")
    time.sleep(1)

def answer2():
    tts = ALProxy("ALTextToSpeech", ROBOT_IP, ROBOT_PORT)
    tts.setLanguage("Japanese")
    tts.setParameter("speed", 1.2)
    tts.say("そうですね")
    time.sleep(1)

def answer3():
    tts = ALProxy("ALTextToSpeech", ROBOT_IP, ROBOT_PORT)
    tts.setLanguage("Japanese")
    tts.setParameter("speed", 1.0)
    tts.say("へえ？")
    time.sleep(1)

def answer4():
    tts = ALProxy("ALTextToSpeech", ROBOT_IP, ROBOT_PORT)
    tts.setLanguage("Japanese")
    tts.setParameter("speed", 1.2)
    tts.say("なるほど")
    time.sleep(1)

options = {
    0 : answer1,
    1 : answer2,
    2 : answer3,
    3 : answer4
}

class ActionThread(threading.Thread):
    def run(self):
        host = 'localhost'
        port = 23000
        buffersize = 4096
        norm_queue = list()
        #r_nodding_flag = 0
        global counter
        timeArray = time.localtime(time.time())
        file_time_stamp = time.strftime("%Y%m%d%H%M%S", timeArray)
        start_time_human = 0
        start_time_robot = 0
        global start_record_flag
        #Human's nod times (Total) for recording
        nod_times = 0

        #振动周期,0.2秒*(t+1) 1周期
        t = 0

        motion = ALProxy ('ALMotion', ROBOT_IP, ROBOT_PORT)
        # Set stiffness on for Head motors
        # Will go to 1.0 then 0 radian
        # in two seconds
        motion.setStiffnesses ('Head', 1.0)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        with closing(sock):
            sock.connect((host, port))
            sock.send('start\n')
            ##sock.send(b'stop\r\n')
            while 1:
                sum_norm = 0
                sum_count = 0
                #Sampling周期20ms，5次=0.1s取平均
                for i in range(0, 5):
                    buffstr = sock.recv(buffersize).replace('\x00', '')
                    bufflist = buffstr.split(',')
                    try:
                        acc_time = float(bufflist[1])
                        acc_x = float(bufflist[2])
                        acc_y = float(bufflist[3])
                        acc_z = float(bufflist[4])
                        #print(bufflist[1] + ',' + bufflist[2] + ',' + bufflist[4])
                        if start_time_human != 0:
                            f1 = open('Reactive_human' + file_time_stamp + '.csv', 'a')
                            f1.writelines(str(acc_time - start_time_human) + ',' + str(round(math.sqrt(acc_x ** 2 + acc_y  ** 2 + acc_z ** 2), 2)) + '\n')
                            f1.close()
                        sum_norm += math.sqrt(acc_x ** 2 + acc_y **2 + acc_z ** 2) 
                        #sum_norm += math.sqrt(acc_x ** 2 + acc_z ** 2)
                        sum_count += 1
                    except BaseException, err:
                        print(err)

                avg_norm = round(sum_norm / sum_count , 2)

                norm_queue.append(avg_norm)
                #超过100项排除第1项
                if len(norm_queue) > 100:
                    norm_queue.pop(0)

                avg_norm_queue = round(sum(norm_queue) / len(norm_queue), 2)
                print('Acc_Time: {0}'.format(str(acc_time)))
                print('Human Start Time: {0}'.format(str(start_time_human)))
                print('Time: {0}'.format(str(acc_time - start_time_human)))
                print('Current: {0}'.format(str(norm_queue[len(norm_queue) - 1])))
                print('Last 10s avg: {0}'.format(str(avg_norm_queue)))

                #if  r_nodding_flag == 0:
                #    if norm_queue[len(norm_queue) - 1] <= (avg_norm_queue - 500) or norm_queue[len(norm_queue) - 1] >= (avg_norm_queue + 500):
                #        r_nodding_flag = 1
                #else :
                #    r_nodding_flag = 0
                if t == 0:
                    #if avg_norm < (avg_norm_queue - 300):
                    if avg_norm_queue - avg_norm > 300:   
                        try:
                            nod_times += 1
                            print('Nod! {0}'.format(nod_times))
                            #if counter > 0:
                            #    counter -= 1
                            #nod's lowest point is after 0.1s
                            record_time_robot = time.time() * 1000 + 100

                            if start_time_human == 0:
                                start_time_human = acc_time
                                start_time_robot = record_time_robot
                            else:
                                f2=open('Reactive_robot' + file_time_stamp + '.csv', 'a')
                                f2.writelines(str(record_time_robot - start_time_robot) + '\n')
                                f2.close()

                            motion.post.angleInterpolation (
                                ['HeadPitch'],
                                [0.0, 0.1, 0.0],
                                [0.001, 0.1, 0.2],
                                False
                            )
                            #阻塞次数
                            t = 1
                        except BaseException, err:
                            print(err)
                else:
                    #低频阻塞处理
                    t -= 1
                    time.sleep(0.2)

        # Gently set stiff off for Head motors
        motion.setStiffnesses ('Head', 0.0)
        return

class VoiceThread(threading.Thread):
    def run(self):
        global counter
        while 1:
            if counter <= 0:
                i = random.randint(0, 3)
                counter = random.randint(7, 10)
                options[i]()
                time.sleep(1)

def main():
    action_threading = ActionThread()
    voice_threading = VoiceThread()
    action_threading.start()
    voice_threading.start()

if __name__ == '__main__':
    main()

