import os
import random
import pygame
import math
import sys
from os import listdir
from os.path import isfile, join
from global_variables import *
from backgroudFunc import *
from playerClass import *
from objectClass import *

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
        window.fill(BG_COLOR if 'BG_COLOR' in globals() else (94, 129, 162))
        
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

# Funcția care creează ecranul și rulează jocul
def main(window):
    clock = pygame.time.Clock()
    
    # --- PASUL 1: RULĂM MENIUL ---
    main_menu(window)
    # -----------------------------

    # Aici se declară toate tipurile de bg
    background, bg_image = get_background("beigeTile.png")
    player = Player(100, 100, 50, 50)
    walls = [Block(0, HEIGHT-100, 100)]
    traps = [Trap(200, 200, 50, 50)]

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    player.take_damage(10) # Scade 10 HP la fiecare apăsare
        
        player.loop(FPS, walls,traps)
        handle_move(player)
        draw(window, background, bg_image, player, walls+traps)
        draw_health_bar(window, player)
        pygame.display.update()

    pygame.quit()
    sys.exit() # Folosim sys.exit() pentru a închide curat

if __name__ == "__main__":
    main(window)