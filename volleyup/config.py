#!/usr/bin/env python

TEMPLATE_DIR = 'data/templates/'
STUB_DIR = 'data/stub/'
PANORAMA_DIR = 'data/panorama/'
DATA_DIR = 'data/'
INPUT_DATA = 'data/beachVolleyballFull.mov'
INPUT_IMGS = 'data/beachVolleyballFull'
INDVIDUAL_VIDEOS = {'{}'.format(i): 'data/beachVolleyball{}'.format(i) for i in range(1, 8)}

'''BGR COLOR CODES'''
RED = [0, 0, 255]
BLUE = [255, 128, 0]
YELLOW = [0, 255, 255]
GREEN = [0, 255, 0]
ORANGE = [0, 69, 255]
PURPLE = [204, 0, 204]
WHITE = [255, 255, 255]

''' OBJECT HSV COLOR RANGES '''
OBJECT_COLOR = {'court': [(20, 0, 100), (50, 100, 255)]}

# Volleyball Court setting
FULL_COURT = (800, 400)
