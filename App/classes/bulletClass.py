import os
import random
import pygame
import math
class bullet_class(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)