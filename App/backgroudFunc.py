import os
import random
import pygame
import math
from os import listdir
from os.path import isfile,join
from global_variables import x_perete,y_perete,matrice_fundal,WIDTH,HEIGHT,FPS,LIGHT_BLUE,PLAYER_VELOCITY
pygame.init()
pygame.display.set_caption("game")
window = pygame.display.set_mode((WIDTH,HEIGHT))


#function for getting a tile and positon vector for background
def get_background(fundal,zid):
    #
    image = pygame.image.load(join("assets","Background",fundal))
    perete = pygame.image.load(join("assets","Background",zid))
    _, _, width, height = image.get_rect() #gaseste marimea imaginii
    tiles=[]
    cnt = 0 # cnt si iful sunt momentan pt a genera o matrice
    cnt2 = 0
    #vor fi eliminate cand facem matricile si layoutul fundalului de mana
    for i in range (WIDTH // width + 1):
        for j in range (HEIGHT // height + 1):
            if(i % 2 == 0 and j % 2 == 0):
                matrice_fundal[cnt] = 1
                x_perete[cnt2] = (i * 100)
                y_perete[cnt2] = (j * 100)
                cnt2 += 1
            pos = (i * width,j* height) #tiles position 
            tiles.append(
                pos)
            cnt = cnt + 1
    return tiles,image,perete

#face loop walls toate pozitiile din fundal si pune bg acolo
def draw(window,background,bg_image1,bg_image_2,player):
    cnt = 0
    for tile in background:
        if(matrice_fundal[cnt] == 1):
            window.blit(bg_image_2,tile)
        else:
            window.blit(bg_image1,tile)
        cnt = cnt + 1

    player.draw(window)
    pygame.display.update()

