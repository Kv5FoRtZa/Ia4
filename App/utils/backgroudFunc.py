import os
import random
import pygame
import math
from os import listdir
from os.path import isfile,join
from utils.global_variables import x_perete,y_perete,matrice_fundal,WIDTH,HEIGHT,FPS,LIGHT_BLUE,PLAYER_VELOCITY
from classes.gameMapClass import GameMap
from classes.levelClass import Level
from utils.global_variables import WIDTH, HEIGHT

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

def draw(window, background_tiles, bg_image, player, current_level, bullets, enemy_b,game_map,boss_b,split_bullets):
    # punem background 
    for tile in background_tiles:
        window.blit(bg_image, tile)

    # desenam walls si traps conform layoutului
    game_map = current_level.getMap() 
    if game_map:
        game_map.draw(window)

    # desenam rd-ei si bullets 
    for bullet in bullets:
        bullet.draw(window)
    for bullet in enemy_b:
        bullet.draw(window)
    for bullet in boss_b:
        bullet.draw(window)
    for bullet in split_bullets:
        bullet.draw(window)
    for i in range(len(game_map.inamic)):
        if (game_map.inamic[i].hp > 0):
            game_map.inamic[i].draw(window,game_map)

    # desenam playerul
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

def draw_boss_bar(window, boss):
    bar_width = WIDTH // 3
    bar_height = 15
    x_pos = WIDTH // 3
    y_pos = 150
    
    ratio = boss.hp / 20
    fill_width = ratio * bar_width
    
    border_rect = pygame.Rect(x_pos, y_pos, bar_width, bar_height)
    
    fill_rect = pygame.Rect(x_pos, y_pos, fill_width, bar_height)
    
    pygame.draw.rect(window, (255, 0, 0), border_rect)
    pygame.draw.rect(window, (255, 255, 255), fill_rect)
    
    pygame.draw.rect(window, (0, 0, 0), border_rect, 2)