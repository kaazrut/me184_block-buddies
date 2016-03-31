# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:34:02 2016

@author: turzaak
"""
import RPi.GPIO as GPIO
import time
import qr_reader

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

qrcode = qr_reader.qrdat()

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