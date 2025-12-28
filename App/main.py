import os
import random
import pygame
import math
import sys
from os import listdir
from os.path import isfile, join
from utils.global_variables import *
from utils.backgroudFunc import *
from classes.playerClass import *
from classes.objectClass import *
from level_menu import levels_menu
from classes.levelClass import *
from classes.gameMapClass import GameMap

pygame.init()
pygame.font.init() # Inițializăm modulul de fonturi

pygame.display.set_caption("PinkMan Adventure")
window = pygame.display.set_mode((WIDTH, HEIGHT)) 

def get_font(size): 
    return pygame.font.SysFont("comicsans", size)

def main_menu(window):
    run = True
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(FPS)
        window.fill((94, 129, 162))
        
        # 1. Titlul
        title_font = get_font(100)
        title_text = title_font.render("PINKMAN ADVENTURE", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(WIDTH/2, 200))
        window.blit(title_text, title_rect)

        instruct_font = get_font(50)
        instruct_text = instruct_font.render("Click to Play", True, (200, 200, 200))
        instruct_rect = instruct_text.get_rect(center=(WIDTH/2, HEIGHT/2))
        window.blit(instruct_text, instruct_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() # Iese de tot din program
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if instruct_rect.collidepoint(mouse_pos):
                    run = False

# TODO: in loc de 1, 2, 3 trebuie sa cream hartile nivelelor 
def create_levels():
    # Level("unlocked", 0, create_map(1))
    # si in create_map(1) -- gameMap() --apelam constructorul clasei : propun sa se num gameMap
    # 1 / 2 / 3 -- dificultatea nivelului (mai multe spike uri / trapuri etc)

    # 18 coloane (1800/100) si 10 randuri (1000/100)
    # am facut tiles de 100 -- putem decide sa fie mai mici
    layout1 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    map1 = GameMap(layout1, tile_size=100)

    levels = [
        Level("Level 1", "unlocked", 0, map1),
        Level("Level 2", "locked", 0, None),
        Level("Level 3", "locked", 0, None)
    ]
    return levels

# Funcția care creează ecranul și rulează jocul
def main(window):
    clock = pygame.time.Clock()
    
    # --- PASUL 1: RULĂM MENIUL ---
    main_menu(window)
    # -----------------------------

    # Levels array and displaying the levels' menu
    levels = create_levels()
    levels_menu(window, levels)

    # current level and it's game_map
    current_level = levels[0]
    game_map = current_level.getMap()

    # Aici se declară toate tipurile de bg
    background_tiles, bg_image = get_background("beigeTile.png")
    player = Player(100, 100, 50, 50)

    run=True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    player.take_damage(10) # Scade 10 HP la fiecare apăsare
        
        # rulam frumos playerul si sa se miste frumos
        player.loop(FPS, game_map.walls, game_map.traps)
        handle_move(player)

        # am facut o functie noua de draw in backgroundFunc 
        # OBS - am pastrat si draw ul vechi in caz de (se numeste draw_vechi)
        draw(window, background_tiles, bg_image, player, current_level)

        # desenam health bar
        draw_health_bar(window, player)
        
        pygame.display.update()

    pygame.quit()
    sys.exit() # Folosim sys.exit() pentru a închide curat

if __name__ == "__main__":
    main(window)