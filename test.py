import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
RGB = [21,20,12,16]
for pin in RGB:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin,GPIO.HIGH)

R=21
G=20
B=12

GPIO.output(R, GPIO.LOW)
