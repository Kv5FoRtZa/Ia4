import os
import random
import pygame
import math
import time
from os import listdir
from os.path import isfile,join
from classes.bulletClass import *
class enemy(object):
    walk = [pygame.image.load(join("assets","MainCharacters","RD","RD.png"))]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hp = 2
    def draw(self, win):
        self.move()
        win.blit((self.walk[0]), (self.x,self.y))
    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
    def fire(self,facing):
        bullets = []
        if len(bullets) < 4:
             bullets.append(bullet_class(round(self.x + 25), round(self.y + 25), 6, (255,0,0), facing)) 
    def damage(self):
        self.hp -= 1
        if self.hp == 0:
            self.x = -1000
            self.y = -1000