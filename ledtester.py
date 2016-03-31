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

<<<<<<< HEAD
GPIO.output(LED, True)

time.sleep(4)

GPIO.output(LED, False)
=======
GPIO.output()
>>>>>>> 2d12dc4e3657bfb0285912fe5febb8b8a2761a3b
