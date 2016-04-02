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


blueLED = 18
redLED = 21
greenLED = 23

#initialize I/Os
GPIO.setmode(GPIO.BCM)
GPIO.setup(blueLED, GPIO.OUT)
GPIO.setup(redLED,GPIO.OUT)
GPIO.setup(greenLED,GPIO.OUT)

#init pwm
redPWM = GPIO.PWM(redLED, 50)
greenPWM = GPIO.PWM(greenLED, 50)
bluePWM = GPIO.PWM(blueLED, 50)
#duty cycle set to 0%
redPWM.start(0)
greenPWM.start(0)
bluePWM.start(0)

#create variables and lists
colorSelect = ("blue", "yellow", "orange", "purple")
colorList = random.sample(colorSelect, 3)
scannedList = []

colorKey = {'blue': {'mp3': 'blue.mp3', 'valR': 0, 'rPul': 0, 'valG': 0, \
            'gPul': 0, 'valB': 1, 'bPul': 100},
            'yellow': {'mp3': 'yellow.mp3', 'valR': 1, 'rPul': 100,'valG': 1, \
            'gPul': 100, 'valB': 0, 'bPul': 0},
            'orange': {'mp3': 'orange.mp3', 'valR': 1, 'rPul': 100, 'valG': 1, \
            'gPul': 50, 'valB': 0, 'bPul': 0},
            'purple': {'mp3': 'purple.mp3', 'valR': 1, 'rPul': 100, 'valG': 0, \
            'gPul': 0, 'valB': 1, 'bPul': 100}
            }

#at startup, run greeting
SOUND_PATH = os.path.join("audio", "mp3")
os.system('mpg123 -q ' + os.path.join(SOUND_PATH, 'IntroHello.mp3 &'))
time.sleep(3)

#Throw everything into a while loop

os.system('mpg123 -q ' + os.path.join(SOUND_PATH, 'NeedHelp.mp3 &'))
time.sleep(1)

#in loop, for each color selected, light the led and say the color
for x in colorList:
   mp3Sel = colorKey[x]['mp3']
   cmd = 'mpg123 -q .' + os.path.join(SOUND_PATH, mp3Sel)
   redPWM.ChangeDutyCycle(colorKey[x]['rPul'])
   GPIO.output(redLED, colorKey[x]['valR'])
   greenPWM.ChangeDutyCycle(colorKey[x]['gPul'])
   GPIO.output(greenLED, colorKey[x]['valG'])
   bluePWM.ChangeDutyCycle(colorKey[x]['bPul'])
   GPIO.output(blueLED, colorKey[x]['valB']) 
   os.system(cmd)
   time.sleep(2)
   GPIO.output(redLED, 1)
   GPIO.output(greenLED, 1)
   GPIO.output(blueLED, 1)
   time.sleep(1)
   

#finish list
os.system('mpg123 -q ' + os.path.join(SOUND_PATH, 'CanOrderBlocks.mp3 &'))


#start checking for qr codes and then append them to a list
qrcode = qr_reader.qrdat()
scannedList.append(qrcode)

if colorList == scannedList:
    #play correct
    pass
else:
    #play inccorect, let them retry all qr code scanning
    pass

ledcheck = 1

testcolor = "blue"

if testcolor == qrcode:
    GPIO.output(23,GPIO.LOW)
    GPIO.output(21,GPIO.HIGH)
    
else:
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(21,GPIO.LOW)
    
time.sleep(10)
GPIO.output(23,GPIO.LOW)
GPIO.output(21,GPIO.HIGH)    

