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

#initialize I/Os
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

#create variables and lists
colorSelect = ("blue", "yellow", "orange", "purple")
colorList = random.sample(colorSelect, 3)
scannedList = []

colorKey = {'blue': {'mp3': 'blue.mp3', 'ledR': 0, 'ledG': 0, 'ledB': 1},
            'yellow': {'mp3': 'yellow.mp3', 'valR': 1, 'valG': 1, 'valB': 0},
            'orange': {'mp3': 'orange.mp3', 'valR': 1, 'valG': 0.5, 'valB': 0},
            'purple': {'mp3': 'purple.mp3', 'valR': 1, 'valG': 0, 'valB': 1}
            }

#at startup, run greeting
SOUND_PATH = os.path.join("audio", "mp3")
os.system('mpg123 -q .\audio\mp3\IntroHello.mp3 &')
time.sleep(3)

#Throw everything into a while loop

os.system('mpg123 -q .\audio\mp3\NeedHelp.mp3 &')
time.sleep(1)

#insert the three random colors
#TODO while loop
#for x in colorList:
   mp3Sel = colorKey[x]['mp3']
   cmd = 'mpg123 -q .' + SOUND_PATH + mp3Sel'
   ledR = colorKey[x]['valR']
   ledG = colorKey[x]['valG']
   ledB = colorKey[x]['valB']
   os.system(cmd)
   time.sleep(2)

#play sound
#wait
#repeat
#os.system('mpg123 -q .\audio\mp3\blue.mp3 &')
#time.sleep(1)
#os.system('mpg123 -q .\audio\mp3\yellow.mp3 &')
#time.sleep(1)
#os.system('mpg123 -q .\audio\mp3\yellow.mp3 &')
#time.sleep(3)

#finish list
os.system('mpg123 -q .\audio\mp3\CanOrderBlocks.mp3 &')


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

