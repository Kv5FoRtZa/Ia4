import pygame
import random
from utils.global_variables import WIDTH, HEIGHT
from classes.enemyClass import *
from classes.levelClass import *
from classes.gameMapClass import *
from classes.playerClass import *

def get_font(size): 
    return pygame.font.SysFont("comicsans", size)

def winning_message(window):
    win_font = get_font(100)
    win_text = win_font.render("LEVEL COMPLETE!", True, (255, 215, 0))
    win_rect = win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    window.blit(overlay, (0,0))
    
    window.blit(win_text, win_rect)
    pygame.display.update()

def losing_message(window):
    win_font = get_font(100)
    win_text = win_font.render("YOU LOST!", True, (255, 0, 0))
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

    layout2 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, -1, -1, -1, -1, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    map2 = GameMap(layout2, tile_size=100)

    layout3 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 1, -1, -1, -1, -1, 1, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, -1, -1, -1, -1, 1, 0, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    map3 = GameMap(layout3, tile_size=100)

    levels = [
        Level("Level 1", "unlocked", 0, map1),
        Level("Level 2", "locked", 0, map2),
        Level("Level 3", "locked", 0, map3)
    ]
    return levels

def create_rd(rand_X, nr_rd,game_map):
    rd = []
    x = random.randint(20,60)
    y = random.randint(20,60)
    copie = x
    for i in range(1,nr_rd):
        x += copie
        y += x
        nu_fi_identic = random.randint(30,50)
        rand_X[i] = random.randint(10,30)
        vf = 0
        for j in range(len(game_map.walls)):
            if square_square_overlap(game_map.walls[j].x + 50,game_map.walls[j].y + 50,100,x + 32,y + 32,64):
                vf = 1
        if vf == 0:
            rd.append(enemy(x, y, 64, 64, 300 + 2 * x + nu_fi_identic))
        else:
            nr_rd  = nr_rd + 1

    return rd

def check_win_condition(rd, nr_rd):
    if not rd:
        return True
    
    for i in range(1, nr_rd - 1):
        if (rd[i].hp > 0):
            return False
    return True

def check_loss_condition(player):
    return player.hp == 0

def unlock_next_level(won_level, levels):
    # unlock la level 2
    if won_level.getName() == "Level 1":
        levels[1].setState("unlocked")
    # unlock la level 3
    if won_level.getName() == "Level 2":
        levels[2].setState("unlocked")
    # dam create la boss level
    #if won_level.getName == "Level 3":
        #create_boss_level()