import os
import random
import pygame
import variables
import math
from os import listdir
from os.path import isfile,join
WHITE=(255,255,255)
BLACK=(0,0,0)
LIGHT_BLUE   = (173, 216, 230)  
BLUE_MUTED   = (70, 130, 180)   
LIGHT_PINK   = (255, 182, 193)  
DARK_GREEN   = (0, 100, 0)
WIDTH=1800
HEIGHT=1000
FPS=60
PLAYER_VELOCITY=5

pygame.init()

pygame.display.set_caption("game")
window = pygame.display.set_mode((WIDTH,HEIGHT))


#function for getting a tile and positon vector for background
def get_background(tile_name):
    image = pygame.image.load(join("assets","Background",tile_name))
    _, _, width, height = image.get_rect() #gets image's width and height
    tiles=[]

    for i in range (WIDTH // width + 1):
        for j in range (HEIGHT // height + 1):
            pos = (i * width,j* height) #tiles position 
            tiles.append(pos)

    return tiles,image

#loop trough all positions and put the tile there
def draw(window,background,bg_image,player):
    for tile in background:
        window.blit(bg_image,tile)

    player.draw(window)

    pygame.display.update()

#ia pozele cu animatia si le face sa fie spre stanga ca ele sunt spre dreapta default
def flip(sprites):
    return [pygame.transform.flip(sprite,True,False) for sprite in sprites]


#loads images
def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites

#player
class Player(pygame.sprite.Sprite):
    COLOR=LIGHT_BLUE
    ANIMATION_DELAY=5
    SPRITES=load_sprite_sheets("MainCharacters","PinkMan",32,32,True)
    def __init__(self,x,y,width,height):
        self.rect = pygame.Rect(x,y,width,height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
    def move(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self,vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self,vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0
    def move_up(self,vel):
        self.y_vel = -vel

    def move_down(self,vel):
        self.y_vel = vel

    #called once per frame to move caracter
    def loop(self,fps):
        self.move(self.x_vel,self.y_vel)
        self.update_sprite()

    def update_sprite(self):
        sprite_sheet = "idle"
        if self.x_vel!=0:
            sprite_sheet = "run"
        if self.y_vel!=0:
            sprite_sheet = "run"

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = self.animation_count//self.ANIMATION_DELAY % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count +=1


    def draw(self,window):
        #pygame.draw.rect(window,self.COLOR,self.rect)

        window.blit(self.sprite,(self.rect.x,self.rect.y))


def handle_move(player):
    keys = pygame.key.get_pressed()
    player.x_vel=0
    player.y_vel=0

    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VELOCITY)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VELOCITY) 
    if keys[pygame.K_UP]:
        player.move_up(PLAYER_VELOCITY)
    if keys[pygame.K_DOWN]:
        player.move_down(PLAYER_VELOCITY)

#functia care creeaza ecranul si da quit
def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("beigeTile.png")
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
        draw(window, background,bg_image,player)

    pygame.quit()
    quit()





if __name__ == "__main__":
    main(window)
