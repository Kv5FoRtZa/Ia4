from os import environ

# it stops showing the pygame message 
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = ''

# importing the required libraries
import pygame
import sys
import time
from pygame.locals import *

# initiating the pygame window 
pygame.init()

## global variables 

# Surface size 
width = 1024 # idk marimea yet - se poate modifica
height = 1024 

# Colors used throughout the project 
white = (255, 255, 255)
black = (0, 0, 0)

# frames per second and time tracker 
fps = 30
CLOCK = pygame.time.Clock()

# setting up the Surface size 
screen = pygame.display.set_mode((width, height), 0, 32)
