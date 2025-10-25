import os
import random
import pygame
import math
from os import listdir
from os.path import isfile,join
from global_variables import *
from backgroudFunc import *
from playerClass import *
pygame.init()
pygame.display.set_caption("game")
window = pygame.display.set_mode((WIDTH,HEIGHT))


#functia care creeaza ecranul si da quit
def main(window):
    clock = pygame.time.Clock()
    #aici se declara toate tipurile de bg
    background, bg_image, perete = get_background("beigeTile.png","crate.png")
    player = Player(100,100,50,50)
    run=True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run=False
                break
        player.loop(FPS)
        handle_move(player)
        draw(window, background,bg_image,perete,player)

    pygame.quit()
    quit()



if __name__ == "__main__":
    main(window)
