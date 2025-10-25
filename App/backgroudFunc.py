import os
import random
import pygame
import math
from os import listdir
from os.path import isfile,join
from global_variables import x_perete,y_perete,matrice_fundal,WIDTH,HEIGHT,FPS,LIGHT_BLUE,PLAYER_VELOCITY
pygame.init()
pygame.display.set_caption("game")
from playerClass import window


#function for getting a tile and positon vector for background
def get_background(fundal):
    image = pygame.image.load(join("assets","Background",fundal))

    _, _, width, height = image.get_rect() #gaseste marimea imaginii
    tiles=[]
    #vor fi eliminate cand facem matricile si layoutul fundalului de mana
    for i in range (WIDTH // width + 1):
        for j in range (HEIGHT // height + 1):
            pos = (i * width,j* height) #tiles position 
            tiles.append(pos)
    return tiles,image

#face loop walls toate pozitiile din fundal si pune bg acolo
def draw(window,background,bg_image,player,walls):
    cnt = 0
    for tile in background:
            window.blit(bg_image,tile)
    for wall in walls:
            wall.draw(window)

    player.draw(window)
    pygame.display.update()

