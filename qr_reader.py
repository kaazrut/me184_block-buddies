# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: turzaak
"""

import io
import os
import time
import picamera
from PIL import Image
import zbar
import pygame
#import RPi.GPIO as GPIO

def qrdat():
    pygame.init()
    pygame.mixer.init()

    #flashPin = 11

    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(flashPin, GPIO.OUT)

    while True:
        symbol = None        
        #create stream in memory
        stream = io.BytesIO()
        with picamera.PiCamera() as camera:
            #GPIO.output(flashPin, 0)
            camera.start_preview()
            time.sleep(2)
            camera.capture(stream, format='jpeg')
            
        #read content from stream
        #GPIO.output(flashPin, 1)
        stream.seek(0)
        pil = Image.open(stream)
        
        #now create a reader for the stream
        scanner = zbar.ImageScanner()
        
        #configure the reader
        scanner.parse_config('enable')
        
        pil = pil.convert('L')
        width, height = pil.size
        raw = pil.tostring()
        
        #image data wrap
        image = zbar.Image(width, height, 'Y800', raw)
        
        # scan the image for barcodes
        scanner.scan(image)
           
        #if find a barcode   
        # extract results, play ding when found a valid qr code
        for symbol in image:
            pygame.mixer.music.load('./audio/mp3/Electronic_Chime-KevanGC.mp3')
            pygame.mixer.music.play()
            print('decoded', symbol.type, 'symbol', '"%s"' % symbol.data)
        
        # clean up
        del(image)    
        
        if symbol:
            return symbol.data
    #if do not find a barcode run again
    
if __name__ == "__main__":
    print(qrdat())
