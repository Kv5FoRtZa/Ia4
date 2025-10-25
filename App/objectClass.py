import os
import random
import pygame
import math
from os import listdir
from os.path import isfile,join
from backgroudFunc import window
from playerClass import load_sprite_sheets,flip

pygame.init()

class Object(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,name=None):
        super().__init__()
        self.rect=pygame.Rect(x,y,width,height)
        self.image=pygame.Surface((width,height),pygame.SRCALPHA)
        self.width=width
        self.height=height
        self.name=name
        
    def draw(self,width):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y,size,size)
        block = get_block("beigeBrick.png",size)
        self.image.blit(block,(0,0))
        self.mask = pygame.mask.from_surface(self.image)

    
def get_block(img_name,size=100,x_start_img=0,y_start_img=0):
    #imi incarca o imagine cu numele img_name si marimea pe pixeli size care la noi va fii 100*100px pe blocuri
    path = join ("assets","Background",img_name)
    image = pygame.image.load(path).convert_alpha()
    surface=pygame.Surface((size,size),pygame.SRCALPHA,32)
    rect = pygame.Rect(x_start_img,y_start_img,size,size)
    surface.blit(image,(0,0),rect)
    return pygame.transform.scale(surface, (size, size))



