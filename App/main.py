import os
import random
import pygame
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
FPS=25
PLAYER_VELOCITY=5
x_perete = [0] * 90# salvez coltul stanga sus pt fiecare perete(sunt noob si nu stiu sa fac coliziune fara var globala)
y_perete = [0] * 90
matrice_fundal = [0] * 290 # aici o sa avem fundalul codat cu 0 = fundal basic, 1 = perete, -1 = tepi, etc
#momentan este 0 si se baga 1 din loc in loc pentru perete
#in get_background fac acesta initializare momentan, insa ea va trebui facuta de mana(pt a avea o harta care arata ok)
#de retinut ca fiecare poza trebuie trecuta prin get_background
#afisez poze diferite in draw, in functie de ce se afla in matrice momentan
pygame.init()

pygame.display.set_caption("game")
window = pygame.display.set_mode((WIDTH,HEIGHT))


#function for getting a tile and positon vector for background
def get_background(fundal,zid):
    #
    image = pygame.image.load(join("assets","Background",fundal))
    perete = pygame.image.load(join("assets","Background",zid))
    _, _, width, height = image.get_rect() #gaseste marimea imaginii
    tiles=[]
    cnt = 0 # cnt si iful sunt momentan pt a genera o matrice
    cnt2 = 0
    #vor fi eliminate cand facem matricile si layoutul fundalului de mana
    for i in range (WIDTH // width + 1):
        for j in range (HEIGHT // height + 1):
            if(i % 2 == 0 and j % 2 == 0):
                matrice_fundal[cnt] = 1
                x_perete[cnt2] = (i * 100)
                y_perete[cnt2] = (j * 100)
                cnt2 += 1
            pos = (i * width,j* height) #tiles position 
            tiles.append(
                pos)
            cnt = cnt + 1
    return tiles,image,perete

#face loop walls toate pozitiile din fundal si pune bg acolo
def draw(window,background,bg_image1,bg_image_2,player):
    cnt = 0
    for tile in background:
        if(matrice_fundal[cnt] == 1):
            window.blit(bg_image_2,tile)
        else:
            window.blit(bg_image1,tile)
        cnt = cnt + 1

    player.draw(window)
    pygame.display.update()

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
        self.rect = pygame.Rect(x,y,width,height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
    def move(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy
        for i in range(0,len(x_perete)):
            perete_curent = pygame.Rect(x_perete[i], y_perete[i], 100, 100)
            if self.rect.colliderect(perete_curent):
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
        self.move(self.x_vel,self.y_vel)
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
