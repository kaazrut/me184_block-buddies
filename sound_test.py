import time
import pygame
import os

SOUND_PATH = os.path.join('audio', 'mp3')
pygame.mixer.init()

sonic = pygame.mixer.music.load('Sonic_the_Hedgehog_3_IceCapped_OC_ReMix.mp3')
intro = pygame.mixer.music.load(os.path.join(SOUND_PATH, 'Intro.mp3'))
needHelp = pygame.mixer.music.load(os.path.join(SOUND_PATH, 'NeedHelp.mp3'))

pygame.mixer.music.play(0, 0.0)
sonic.play()
intro.queue()
needHelp.queue()