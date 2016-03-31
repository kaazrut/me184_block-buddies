# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import io
import time
import picamera
from PIL import Image
import zbar

#create stream in memory
stream = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    camera.capture(stream, format='jpeg')
    
#read content from stream
stream.seek(0)
pil = Image.open(stream)

#now create a reader for the stream
scanner = zbar.Proessor()

#configure the reader
scanner.parse_config('enable')

pil = pil.convert('L')
width, height = pil.size
raw = pil.tostring()

#image data wrap
image = zbar.Image(width, height, 'Y800', raw)

# scan the image for barcodes
scanner.scan(image)

# extract results
for symbol in image:
    print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
    
def qrdat:
    return symbol
# clean up
del(image)