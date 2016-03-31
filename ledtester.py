# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:52:25 2016

@author: turzaak
"""

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED = 23

GPIO.setup(LED, GPIO.OUT)

GPIO.output(LED, True)

time.sleep(4)

GPIO.output(LED, False)
