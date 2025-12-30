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
from classes.bulletClass import *
from classes.enemyClass import *
from classes.overlapClass import *
from utils.enemyLogicFunc import *

pygame.init()
pygame.font.init() # Inițializăm modulul de fonturi

pygame.display.set_caption("PinkMan Adventure")
window = pygame.display.set_mode((WIDTH, HEIGHT)) 

# BIG TODO: de mutat toate metodele din main intr-un fisier ajutator

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

def winning_message(window):
    win_font = get_font(100)
    win_text = win_font.render("LEVEL COMPLETE!", True, (255, 215, 0))
    win_rect = win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    window.blit(overlay, (0,0))
    
    window.blit(win_text, win_rect)
    pygame.display.update()

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

def create_rd(rand_X, nr_rd):
    rd = []
    x = random.randint(20,60)
    y = random.randint(20,60)
    copie = x
    for i in range(1,nr_rd):
        x += copie
        y += x
        nu_fi_identic = random.randint(30,50)
        rand_X[i] = random.randint(10,30)
        rd.append(enemy(x, y, 64, 64, 300 + 2 * x + nu_fi_identic))

    return rd

def check_win_condition(rd, nr_rd):
    if not rd:
        return True
    
    for i in range(1, nr_rd - 1):
        if (rd[i].hp > 0):
            return False
    return True

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

    # bullets rd-ei si helperi pt ele
    bullets = []
    enemy_bullets = []
    nr_rd = 5
    rand_X = [10, 10, 10, 10, 10, 10, 10]
    rd = create_rd(rand_X, nr_rd)
    cnt_tras = 0

    run=True
    while run:
        cnt_tras += 1
        clock.tick(FPS)

        # handles the shooting logic
        handle_player_bullets_logic(bullets, player, rd, nr_rd)
        handle_enemy_bullets_logic(enemy_bullets, player, rd)
        handle_enemy_shooting(rd, enemy_bullets, cnt_tras, nr_rd, rand_X)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    player.take_damage(10) # Scade 10 HP la fiecare apăsare
            if event.type == pygame.MOUSEBUTTONUP:  # tragere de gloante ale player-ului
                if player.direction == 'left':
                    facing = -1
                else:
                    facing = 1
                if len(bullets) < 16:
                    bullets.append(bullet_class(round(player.rect.x + 25), round(player.rect.y + 25), 6, (0,0,0), facing,0)) 

        # rulam frumos playerul si sa se miste frumos
        player.loop(FPS, game_map.walls, game_map.traps)
        handle_move(player)

        # am facut o functie noua de draw in backgroundFunc -- am bagat rd-ei in ea
        draw(window, background_tiles, bg_image, player, current_level, bullets, rd, enemy_bullets, nr_rd)

        # desenam health bar
        draw_health_bar(window, player)
        
        pygame.display.update()

        # daca s a castigat -- marcam in nivel si ne intoarcem la meniu
        # TODO: a while in a while sa ne intoarcem cu adevarat la meniu
        if check_win_condition(rd, nr_rd) is True:
            draw(window, background_tiles, bg_image, player, current_level, bullets, rd, enemy_bullets, nr_rd)
            pygame.display.update()
            winning_message(window)
            current_level.setWinStatus(1)
            pygame.time.delay(3000)
            run = False

    pygame.quit()
    sys.exit() # Folosim sys.exit() pentru a închide curat

if __name__ == "__main__":
    main(window)