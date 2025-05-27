import sys

import pygame
from pygame.locals import *
import numpy
pygame.init()


# class aproach


# class for ball and paddles



# make window
shouldcont = True

while shouldcont == True:
    for event in pygame.event.get():
        if event.type() == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()