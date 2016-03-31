import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

QR_COLOR = 1

if QR_COLOR == 0:
    GPIO.output(23,GPIO.LOW)
    GPIO.output(21,GPIO.HIGH)
else:
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(21,GPIO.LOW)



time.sleep(2)
GPIO.output(23,GPIO.HIGH)
GPIO.output(21,GPIO.HIGH)
