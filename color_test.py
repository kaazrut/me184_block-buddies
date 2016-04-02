# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 13:17:02 2016

@author: turzaak
"""

import random
import os

colorSelect = ("blue", "yellow", "orange", "purple")
colorList = random.sample(colorSelect, 3)

colorKey = {'blue': {'mp3': 'bluepath', 'ledR': 0, 'ledG': 0, 'ledB': 1},
            'yellow': {'mp3': 'yellowpath', 'ledR': 1, 'ledG': 1, 'ledB': 0},
            'orange': {'mp3': 'orangepath', 'ledR': 1, 'ledG': 0.5, 'ledB': 0},
            'purple': {'mp3': 'purplepath', 'ledR': 1, 'ledG': 0, 'ledB': 1}
            }
