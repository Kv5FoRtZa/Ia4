import os
import random
import pygame
import math
from os import listdir
from os.path import isfile,join
from global_variables import *
from backgroudFunc import *
from playerClass import *
from objectClass import *
pygame.init()
pygame.display.set_caption("game")
from playerClass import window


#functia care creeaza ecranul si da quit
def main(window):
    clock = pygame.time.Clock()
    #aici se declara toate tipurile de bg
    background, bg_image = get_background("beigeTile.png")
    player = Player(100,100,50,50)
    walls=[Block(0,HEIGHT-100,100)]

    run=True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run=False
                break
        player.loop(FPS, walls)
        handle_move(player)
        draw(window, background,bg_image,player,walls)

    pygame.quit()
    quit()



if __name__ == "__main__":
    main(window)
