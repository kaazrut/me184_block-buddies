# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:34:02 2016

@author: turzaak
"""
import RPi.GPIO as GPIO
import time
import qr_reader
import os

#initialize I/Os
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

#create variables and lists
colorSelect = ["blue", "yellow", "orange", "purple"]
colorList = []
scannedList = []

#at startup, run greeting
os.system('mpg123 -q .\audio\mp3\IntroHello.mp3 &')
wait(3)

#Throw everything into a while loop

os.system('mpg123 -q .\audio\mp3\NeedHelp.mp3 &')
wait(1)

#insert the three random colors
#TODO figure out how to randomize that list
os.system('mpg123 -q .\audio\mp3\blue.mp3 &')
wait(1)
os.system('mpg123 -q .\audio\mp3\yellow.mp3 &')
wait(1)
os.system('mpg123 -q .\audio\mp3\yellow.mp3 &')
wait(3)

#finish list
os.system('mpg123 -q .\audio\mp3\CanOrderBlocks.mp3 &')


#start checking for qr codes and then append them to a list
qrcode = qr_reader.qrdat()
scannedList.append(qrcode)

ledcheck = 1

testcolor = "blue"

if testcolor == qrcode:
    GPIO.output(23,GPIO.LOW)
    GPIO.output(21,GPIO.HIGH)
    
else:
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(21,GPIO.LOW)
    
wait(10)
GPIO.output(23,GPIO.LOW)
GPIO.output(21,GPIO.HIGH)    

