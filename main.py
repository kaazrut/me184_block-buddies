# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:34:02 2016

@author: turzaak
"""
import RPi.GPIO as GPIO
import time
import qr_reader
import os
import random
import pygame


redLED = 21
greenLED = 20
blueLED = 12

correctLED = 18 #green
wrongLED = 23   #red 

#restart game 
resetPin = 24

#power pins
pwrRGBled = 16
pwrRGled = 25

#initialize I/Os
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(blueLED, GPIO.OUT)
GPIO.setup(redLED,GPIO.OUT)
GPIO.setup(greenLED,GPIO.OUT)
GPIO.setup(correctLED, GPIO.OUT)
GPIO.setup(wrongLED, GPIO.OUT)

GPIO.setup(pwrRGBled, GPIO.OUT)
GPIO.setup(pwrRGled, GPIO.OUT)

GPIO.setup(resetPin, GPIO.IN)

#init pwm
redPWM = GPIO.PWM(redLED, 50)
greenPWM = GPIO.PWM(greenLED, 50)
bluePWM = GPIO.PWM(blueLED, 50)

#duty cycle set to 0%
redPWM.start(100)
greenPWM.start(100)
bluePWM.start(100)

#initialize power pins
GPIO.output(pwrRGBled, GPIO.HIGH)
GPIO.output(pwrRGled, GPIO.HIGH)

GPIO.output([redLED, greenLED, blueLED], GPIO.LOW)
GPIO.output([wrongLED, correctLED], GPIO.HIGH)

#initalize sound
pygame.init()
pygame.mixer.init()

#create variables and lists
playagain = True

#for led color, 0 = on, 1 = off (this is due to wiring for GPIO)
colorKey = {
    'blue': {
        'wav': 'blue.wav',
        'valR': 0,
        'rPul': 100,
        'valG': 0,
        'gPul': 100,
        'valB': 1,
        'bPul': 0
    },
    'yellow': {
        'wav': 'yellow.wav',
        'valR': 1,
        'rPul': 0,
        'valG': 1,
        'gPul': 50,
        'valB': 0,
        'bPul': 100
    },
    'orange': {
        'wav': 'orange.wav',
        'valR': 1,
        'rPul': 0,
        'valG': 1,
        'gPul': 90,
        'valB': 0,
        'bPul': 100
    },
     'purple': {
        'wav': 'purple.wav',
        'valR': 1,
        'rPul': 0,
        'valG': 0,
        'gPul': 100,
        'valB': 1,
        'bPul': 0
    }
}

colorSelect = tuple(colorKey.keys())

#at startup, load all sound files
SOUND_PATH = os.path.join('audio', 'wav')

intro = pygame.mixer.Sound(os.path.join(SOUND_PATH, 'IntroHello.wav'))
needhelp = pygame.mixer.Sound(os.path.join(SOUND_PATH, 'NeedHelp.wav'))
tower = pygame.mixer.Sound(os.path.join(SOUND_PATH, 'Tower.wav'))
orderblocks = pygame.mixer.Sound(os.path.join(SOUND_PATH, 'CanOrderBlocks.wav'))
allright = pygame.mixer.Sound(os.path.join(SOUND_PATH, 'AllBlocksRight.wav'))
blockswrong = pygame.mixer.Sound(os.path.join(SOUND_PATH, 'AllBlocksWrong.wav'))
closeout = pygame.mixer.Sound(os.path.join(SOUND_PATH, 'CloseOut.wav'))

for x in colorKey:
    colorKey[x]['load'] = pygame.mixer.Sound(os.path.join(SOUND_PATH, colorKey[x]['wav']))

#start sound
channel = pygame.mixer.Channel(0)
channel.queue(intro)
channel.set_volume(1.0)

def gametime():
    global playagain
    
    while channel.get_queue() or channel.get_busy():
        time.sleep(0.1)

    channel.queue(needhelp)
    #pygame.mixer.Sound(os.path.join(SOUND_PATH, 'NeedHelp.wav &'))
    #time.sleep(3)

    #in loop, for each color selected, light the led and say the color
    colorList = random.sample(colorSelect, 3)

    for x in colorList:
        channel.queue(colorKey[x]['load'])
        while channel.get_queue() or channel.get_busy():
            time.sleep(0.1)
        redPWM.ChangeDutyCycle(colorKey[x]['rPul'])
        GPIO.output(redLED, colorKey[x]['valR'])
        greenPWM.ChangeDutyCycle(colorKey[x]['gPul'])
        GPIO.output(greenLED, colorKey[x]['valG'])
        bluePWM.ChangeDutyCycle(colorKey[x]['bPul'])
        GPIO.output(blueLED, colorKey[x]['valB']) 
        GPIO.output(redLED, 1)
        GPIO.output(greenLED, 1)
        GPIO.output(blueLED, 1)
        time.sleep(1)
       
    while channel.get_queue() or channel.get_busy():
        time.sleep(0.1)
        
    time.sleep(0.1)
    #finish list
    redPWM.ChangeDutyCycle(100)
    greenPWM.ChangeDutyCycle(100)
    bluePWM.ChangeDutyCycle(100)
    channel.queue(tower)
    channel.queue(orderblocks)

    time.sleep(3)
    
    #start checking for qr codes and then append them to a list
    def qrscan():
        scannedList = []
        for x in colorList:
            qrcode = qr_reader.qrdat()
            scannedList.append(qrcode)
        return scannedList    

    check = True

    while check:
        if colorList == qrscan():
            #play correct
            GPIO.output(correctLED, 0)
            GPIO.output(wrongLED, 1)
            channel.queue(allright)
            check = False
            
            reset = GPIO.wait_for_edge(resetPin, GPIO.BOTH, timeout = 10000)
            if reset is None:
                playagain = False
                channel.queue(closeout)
                time.sleep(5)
                GPIO.cleanup()

        else:
            #play incorrect, let them retry all qr code scanning
            GPIO.output(wrongLED, 0)
            GPIO.output(correctLED, 1)
            channel.queue(blockswrong)
            time.sleep(2)

#Throw everything into a while loop from this point
while playagain: 
    gametime()
