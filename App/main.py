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
from utils.gameLogicFunc import *

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

def play_game(window, current_level):
    clock = pygame.time.Clock()
    # harta jocului curent
    game_map = current_level.getMap()

    # Aici se declară toate tipurile de bg
    background_tiles, bg_image = get_background("beigeTile.png")
    player = Player(100, 100, 50, 50)

    # bullets rd-ei si helperi pt ele
    bullets = []
    enemy_bullets = []
    nr_rd = 5
    rand_X = [10, 10, 10, 10, 10, 10, 10]
    rd = create_rd(rand_X, nr_rd,game_map)
    cnt_tras = 0

    run=True
    while run:
        cnt_tras += 1
        clock.tick(FPS)

        # handles the shooting logic
        handle_player_bullets_logic(bullets, player, rd, nr_rd,game_map)
        handle_enemy_bullets_logic(enemy_bullets, player, rd,game_map)
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
        draw(window, background_tiles, bg_image, player, current_level, bullets, rd, enemy_bullets, nr_rd,game_map)

        # desenam health bar
        draw_health_bar(window, player)
        
        pygame.display.update()

        # daca s a castigat -- marcam in nivel si ne intoarcem la meniu
        if check_win_condition(rd, nr_rd) is True:
            draw(window, background_tiles, bg_image, player, current_level, bullets, rd, enemy_bullets, nr_rd,game_map)
            winning_message(window)
            current_level.setWinStatus(1)
            pygame.time.delay(3000)
            run = False

        if check_loss_condition(player) is True:
            draw(window, background_tiles, bg_image, player, current_level, bullets, rd, enemy_bullets, nr_rd,game_map)
            losing_message(window)
            pygame.time.delay(3000)
            run = False

# Funcția care creează ecranul și rulează jocul
def main(window):
    clock = pygame.time.Clock()
    
    # --- PASUL 1: RULĂM MENIUL ---
    main_menu(window)
    # -----------------------------

    # Levels array and choosing a level
    levels = create_levels()
    run = True

    while run:
        # displaying the levels' menu and choosing to play a level
        current_level = levels_menu(window, levels)

        if current_level:
            play_game(window, current_level)
            if current_level.getWinStatus() == 1:
                unlock_next_level(current_level, levels)
        else:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()
    sys.exit() # Folosim sys.exit() pentru a închide curat

if __name__ == "__main__":
    main(window)