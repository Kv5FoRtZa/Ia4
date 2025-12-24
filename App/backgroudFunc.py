import os
import random
import pygame
import math
from os import listdir
from os.path import isfile,join
from global_variables import x_perete,y_perete,matrice_fundal,WIDTH,HEIGHT,FPS,LIGHT_BLUE,PLAYER_VELOCITY
pygame.init()
pygame.display.set_caption("game")


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

def draw_health_bar(window, player):
    # Configurare bara
    bar_width = 200
    bar_height = 20
    x_pos = 20  # Distanța de la stânga ecranului
    y_pos = 20  # Distanța de sus
    
    # Calculăm cât din bară trebuie să fie verde (procentaj)
    # Formula: (HP curent / HP maxim) * Lățime totală
    ratio = player.hp / player.max_hp
    fill_width = ratio * bar_width
    
    # Dreptunghiul de fundal (Roșu - arată cât damage ai luat)
    border_rect = pygame.Rect(x_pos, y_pos, bar_width, bar_height)
    
    # Dreptunghiul de viață (Verde - arată câtă viață mai ai)
    fill_rect = pygame.Rect(x_pos, y_pos, fill_width, bar_height)
    
    # Desenăm dreptunghiurile
    pygame.draw.rect(window, (255, 0, 0), border_rect) # Fundal Roșu
    pygame.draw.rect(window, (0, 255, 0), fill_rect)   # Viață Verde
    
    # Opțional: Un contur alb pentru aspect mai plăcut
    pygame.draw.rect(window, (255, 255, 255), border_rect, 2)
