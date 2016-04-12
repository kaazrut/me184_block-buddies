import time
import pygame
import os
import random

SOUND_PATH = os.path.join('audio', 'wav')
pygame.init()
pygame.mixer.init()

#pygame.mixer.music.load('Sonic_the_Hedgehog_3_IceCapped_OC_ReMix.mp3')
intro = pygame.mixer.Sound(os.path.join(SOUND_PATH, 'blue.wav'))
needHelp = pygame.mixer.Sound(os.path.join(SOUND_PATH, 'yellow.wav'))

#pygame.mixer.music.play(0, 0.0)
#channel = pygame.mixer.find_channel()
channel = pygame.mixer.Channel(0)
channel.queue(intro)
#channel.queue(needHelp)
#channel.queue(intro)

#while channel.get_queue() or channel.get_busy():
#    time.sleep(0.1)

while True:
    if not channel.get_queue():
        channel.queue(random.choice((intro, needHelp)))

#intro.queue()
#needHelp.queue()
