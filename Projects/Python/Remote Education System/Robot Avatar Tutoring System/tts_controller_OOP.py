# -*- encoding: UTF-8 -*-
"""tts_controller_OOP controller."""

from controller import Robot, Keyboard, LED, Motion
from multiprocessing import Process
import pyttsx
import sys
import time

# this is the main class
class Nao (Robot):

    # load motion files
    def loadMotionFiles(self):
        self.handWave = Motion('C:/Program Files/Webots/projects/robots/aldebaran/motions/HandWave.motion')

    def startMotion(self, motion):
        # interrupt current motion
        if self.currentlyPlaying:
            self.currentlyPlaying.stop()

        # start new motion
        motion.play()
        self.currentlyPlaying = motion

    def setAllLedsColor(self, rgb):
        # these leds take RGB values
        for i in range(0, len(self.leds)):
            self.leds[i].set(rgb)

        # ear leds are single color (blue)
        # and take values between 0 - 255
        self.leds[5].set(rgb & 0xFF)
        self.leds[6].set(rgb & 0xFF)

    def startUtterance(self):
        # create the speech engine instance.
        reload(sys)
        sys.setdefaultencoding('utf8')
        engine = pyttsx.init()

        # speech properties instantiation
        rate = engine.getProperty('rate') # default rate = 200
        volume = engine.getProperty('volume') # default volume = 1.0
        voices = engine.getProperty('voices')

        # speech properties initialization
        engine.setProperty('rate', 150) # new voice rate 
        engine.setProperty('volume', 1.0) # new volume
        engine.setProperty('voice', voices[2].id) # default speaker = Haruka
        
        engine.say('ネイチャーセンターのナオと申します。本日何をやろうと思いますか？')
        engine.say('自転車に乗る場合は、一を入力して下さい')
        engine.say('走りたい場合は、二を入力して下さい')
        engine.say('登山の場合は、三を入力して下さい。')
        engine.say('やめたい場合は、qを入力して下さい。')
        engine.runAndWait()
    
    def bicycle(self):
        # create the speech engine instance.
        reload(sys)
        sys.setdefaultencoding('utf8')
        engine = pyttsx.init()

        # speech properties instantiation
        rate = engine.getProperty('rate') # default rate = 200
        volume = engine.getProperty('volume') # default volume = 1.0
        voices = engine.getProperty('voices')

        # speech properties initialization
        engine.setProperty('rate', 150) # new voice rate
        engine.setProperty('volume', 1.0) # new volume
        engine.setProperty('voice', voices[2].id) # default speaker = Haruka
        
        engine.say('一を選びました。自転車はこちらです。お楽しみ下さい。')
        engine.runAndWait()
        
    def running(self):
        # create the speech engine instance.
        reload(sys)
        sys.setdefaultencoding('utf8')
        engine = pyttsx.init()

        # speech properties instantiation
        rate = engine.getProperty('rate') # default rate = 200
        volume = engine.getProperty('volume') # default volume = 1.0
        voices = engine.getProperty('voices')

        # speech properties initialization
        engine.setProperty('rate', 150) # new voice rate
        engine.setProperty('volume', 1.0) # new volume
        engine.setProperty('voice', voices[2].id) # default speaker = Haruka
        
        engine.say('二を選びました。スポーツシューズはこちらです。急いで走って下さい。')
        engine.runAndWait()
    
    def mountain(self):
        # create the speech engine instance.
        reload(sys)
        sys.setdefaultencoding('utf8')
        engine = pyttsx.init()

        # speech properties instantiation
        rate = engine.getProperty('rate') # default rate = 200
        volume = engine.getProperty('volume') # default volume = 1.0
        voices = engine.getProperty('voices')

        # speech properties initialization
        engine.setProperty('rate', 150) # new voice rate
        engine.setProperty('volume', 1.0) # new volume
        engine.setProperty('voice', voices[2].id) # default speaker = Haruka
        
        engine.say('三を選びました。地図はこちらです。予定を作ってくれますか？')
        engine.runAndWait()
    
    def quit(self):
        # create the speech engine instance.
        reload(sys)
        sys.setdefaultencoding('utf8')
        engine = pyttsx.init()

        # speech properties instantiation
        rate = engine.getProperty('rate') # default rate = 200
        volume = engine.getProperty('volume') # default volume = 1.0
        voices = engine.getProperty('voices')

        # speech properties initialization
        engine.setProperty('rate', 150) # new voice rate
        engine.setProperty('volume', 1.0) # new volume
        engine.setProperty('voice', voices[2].id) # default speaker = Haruka
        
        engine.say('四を選びました。ご利用ありがとうございます。ではまたね')
        engine.runAndWait()
    
    def findAndEnableDevices(self):
        # get the time step of the current world.
        self.timeStep = int(self.getBasicTimeStep())

        # there are 7 controlable LED groups in Webots
        self.leds = []
        self.leds.append(self.getLED('ChestBoard/Led'))
        self.leds.append(self.getLED('RFoot/Led'))
        self.leds.append(self.getLED('LFoot/Led'))
        self.leds.append(self.getLED('Face/Led/Right'))
        self.leds.append(self.getLED('Face/Led/Left'))
        self.leds.append(self.getLED('Ears/Led/Right'))
        self.leds.append(self.getLED('Ears/Led/Left'))

        # keyboard
        self.keyboard = self.getKeyboard()
        self.keyboard.enable(10 * self.timeStep)

    def __init__(self):
        Robot.__init__(self)
        self.currentlyPlaying = False

        # initialize stuff
        self.findAndEnableDevices()
        self.loadMotionFiles()

    def run(self):
        # set counter to control robot motion and utterance
        count = 0
        while robot.step(self.timeStep) != -1:
            count += 1
            self.handWave.play()
            
            if (count >= 400):
              self.handWave.stop()
              self.startUtterance()
              print ('\nネイチャーセンターのナオと申します。本日何をやろうと思いますか？')
              print("\n[1] 自転車に乗る場合は、1 を入力して下さい。")
              print("\n[2] 走りたい場合は、2 を入力して下さい。")
              print("\n[3] 登山の場合は、3 を入力して下さい。")
              print("\n[4] やめたい場合は、4 を入力して下さい。")
              time.sleep(1.0)
              break

        while True:
            key = self.keyboard.getKey()
            
            if key == ord('1'):
                self.setAllLedsColor(0xff0000)  # red
                self.bicycle()
            elif key == ord('2'):
                self.setAllLedsColor(0x00ff00)  # green
                self.running()
            elif key == ord('3'):
                self.setAllLedsColor(0x0000ff)  # blue
                self.mountain()
            elif key == ord('4'):
                self.setAllLedsColor(0x000000)  # off
                self.quit()

            if robot.step(self.timeStep) == -1:
                break

# create the Robot instance and run main loop
robot = Nao()
robot.run()
