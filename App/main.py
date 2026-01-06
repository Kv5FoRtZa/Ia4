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
from utils.bossLogicFunc import *
from utils.gameLogicFunc import *
from classes.resetEnemy import *

pygame.init()
pygame.font.init() # Inițializăm modulul de fonturi

pygame.display.set_caption("EVO HUNTER")
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
        title_text = title_font.render("EVO HUNTER", True, (255, 255, 255))
        font = pygame.font.SysFont('Comic Sans MS', 30)
        font2 = pygame.font.SysFont('Comic Sans MS', 70)
        text1 = font.render("Bine ai venit!", False, (200, 200, 200))
        text2 = font.render("In acest joc trebuie sa vanezi goblini mov evil!", False, (200, 200, 200))
        text3 = font.render("Esti singurul care ii poate opri!", False, (200, 200, 200))
        text1_rect = title_text.get_rect(center=(WIDTH/2, 300))
        text2_rect = title_text.get_rect(center=(WIDTH/2, 330))
        text3_rect = title_text.get_rect(center=(WIDTH/2, 360))
        title_rect = title_text.get_rect(center=(WIDTH/2, 200))
        window.blit(text1, text1_rect)
        window.blit(text2, text2_rect)
        window.blit(text3, text3_rect)
        window.blit(title_text, title_rect)

        instruct_font = get_font(90)
        instruct_text = instruct_font.render("Click to Play", True, (200, 200, 200))
        instruct_rect = instruct_text.get_rect(center=(WIDTH/2, HEIGHT/2))
        window.blit(instruct_text, instruct_rect)
        Inst = font2.render("Instructiuni:", False, (200, 200, 200))
        i1 = font.render("Mers pe wasd sau pe sageti", False, (200, 200, 200))
        i2 = font.render("Pentru a impusca apasa click", False, (200, 200, 200))
        Inst_rect = Inst.get_rect(center=(WIDTH/2, 2 * HEIGHT/3))
        I1_rect = Inst.get_rect(center=(WIDTH/2, 2 * HEIGHT/3 + 50))
        I2_rect = Inst.get_rect(center=(WIDTH/2, 2 * HEIGHT/3 + 75))
        window.blit(Inst, Inst_rect)
        window.blit(i1, I1_rect)
        window.blit(i2, I2_rect)
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
    #save = current_level.getMap()

    # Aici se declară toate tipurile de bg
    background_tiles, bg_image = get_background("beigeTile.png")
    player = Player(100, 100, 32, 32)

    # bullets rd-ei si helperi pt ele
    bullets = []
    enemy_bullets = []
    boss_bullets = []
    split_bullets = []
    nr_rd = 5
    rand_X = [10 for _ in range(len(game_map.inamic))]
    rnd = 10
    #rd = create_rd(rand_X, nr_rd,game_map)
    cnt_tras = 0

    run=True
    while run:
        cnt_tras += 1
        clock.tick(FPS)

        # handles the shooting logic
        handle_player_bullets_logic(bullets, player,game_map)
        handle_enemy_bullets_logic(enemy_bullets, player,game_map)
        handle_enemy_shooting(game_map,enemy_bullets, cnt_tras, rand_X)
        if game_map.bosss:
            hanle_boss_shooting(boss_bullets, cnt_tras,rnd,game_map.bosss[0],player)
            handle_boss_bullets_logic(boss_bullets,player,game_map.bosss[0],game_map,split_bullets)
        if len(split_bullets) != 0:
            handle_split_bullets_logic(split_bullets,player,game_map)
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
                    bullets.append(bullet_class(round(player.rect.x + 25), round(player.rect.y + 25), 6, (0,0,0), facing,0,0)) 

        # rulam frumos playerul si sa se miste frumos
        player.loop(FPS, game_map.walls, game_map.traps)
        handle_move(player)

        # am facut o functie noua de draw in backgroundFunc
        draw(window, background_tiles, bg_image, player, current_level, bullets, enemy_bullets,game_map,boss_bullets,split_bullets)

        # desenam health bar
        draw_health_bar(window, player)
        if game_map.bosss:
            draw_boss_bar(window,game_map.bosss[0])

        pygame.display.update()

        # daca s a castigat -- marcam in nivel si ne intoarcem la meniu
        if check_win_condition(game_map) is True:
            draw(window, background_tiles, bg_image, player, current_level, bullets, enemy_bullets,game_map,boss_bullets,split_bullets)
            winning_message(window)
            # should help with the messages who are not always being displayed
            pygame.display.flip() 
            pygame.event.pump()

            current_level.setWinStatus(1)
            reset_map(game_map)
            pygame.time.delay(3000)
            run = False

        if check_loss_condition(player) is True:
            draw(window, background_tiles, bg_image, player, current_level, bullets, enemy_bullets,game_map,boss_bullets,split_bullets)
            losing_message(window)

            pygame.display.flip() 
            pygame.event.pump()

            reset_map(game_map)
            pygame.time.delay(3000)
            run = False

# main function -- rulam jocul
def main(window):
    clock = pygame.time.Clock()
    
    # rulam meniul
    main_menu(window)

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
    sys.exit()

if __name__ == "__main__":
    main(window)