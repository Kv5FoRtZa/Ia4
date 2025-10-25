import os
import random
import pygame
import math
from os import listdir
from os.path import isfile,join
from global_variables import x_perete,y_perete,matrice_fundal,WIDTH,HEIGHT,FPS,LIGHT_BLUE,PLAYER_VELOCITY
pygame.init()
pygame.display.set_caption("game")
window = pygame.display.set_mode((WIDTH,HEIGHT))

#ia pozele cu animatia si le face sa fie spre stanga ca ele sunt spre dreapta default
def flip(sprites):
    return [pygame.transform.flip(sprite,True,False) for sprite in sprites]


#loads images
# SPRITE == imagine pe frames 
def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    # dir1 - director_for_characters
    # dir2 - director_for_pink man in this situation 
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        # .convert_alpha() says they are transparent 
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
        super().__init__()
        self.rect = pygame.Rect(x,y,width,height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
    def move(self,dx,dy,x_wall,y_wall):
        self.rect.x += dx
        self.rect.y += dy
        for i in range(0,len(x_wall)):
            current_wall = pygame.Rect(x_wall[i], y_wall[i], 100, 100)
            if self.rect.colliderect(current_wall):
                self.rect.x -= dx
                self.rect.y -= dy
    
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

    #muta caracterul frame by frame
    def loop(self,fps):
        self.move(self.x_vel,self.y_vel,x_perete,y_perete)
        self.update_sprite()

    # updateaza animatia frame by frame
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

    # afiseaza caracterul
    def draw(self,window):
        window.blit(self.sprite,(self.rect.x,self.rect.y))


def handle_move(player):
    keys = pygame.key.get_pressed()
    player.x_vel=0
    player.y_vel=0
    #merge pe sageti si pe wasd
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
        player.move_left(PLAYER_VELOCITY)
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
        player.move_right(PLAYER_VELOCITY) 
    if (keys[pygame.K_UP] or keys[pygame.K_w]):
        player.move_up(PLAYER_VELOCITY)
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]):
        player.move_down(PLAYER_VELOCITY)