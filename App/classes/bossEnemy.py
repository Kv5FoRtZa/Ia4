import os
import random
import pygame
import math
import time
from os import listdir
from os.path import isfile,join
from classes.bulletClass import *
from classes.overlapClass import *

class boss(object):
    walk = [pygame.image.load(join("assets","MainCharacters","RD","UPB.png"))]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hp = 20
    def draw(self, win,walls):
        self.move(walls)
        win.blit((self.walk[0]), (self.x,self.y))
    def move(self,walls):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                vf = 0
                for i in range(len(walls)):
                     if square_square_overlap(walls[i].x + 50,walls[i].y + 50,100,self.x + self.height / 2,self.y + self.width / 2,self.height):
                         vf = 1
                         break
                if vf == 0:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.x += self.vel
                    self.walkCount = 0
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                vf = 0
                for i in range(len(walls)):
                     if square_square_overlap(walls[i].x + 50,walls[i].y + 50,100,self.x + self.height / 2,self.y + self.width / 2,self.height):
                         vf = 1
                         break
                if vf == 0:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.x += self.vel
                    self.walkCount = 0
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
    def damage(self):
        self.hp -= 1
        if self.hp == 0:
            self.x = -1000
            self.y = -1000