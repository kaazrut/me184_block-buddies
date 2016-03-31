# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:52:25 2016

@author: turzaak
"""

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED = 20

GPIO.setup(LED, GPIO.OUT)

GPIO.output(LED, True)