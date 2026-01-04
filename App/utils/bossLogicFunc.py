import pygame
from classes.overlapClass import *
from classes.bulletClass import bullet_class
from utils.backgroudFunc import *
import sys
from classes.bossBulletClass import *

def hanle_boss_shooting(boss_bullets, cnt_tras, rand_X,boss,player):
    #trage catre directia player-ului
        if (cnt_tras) % int(rand_X) == 0:
            if  abs(boss.x - player.rect.x) < 40:
                if boss.y < player.rect.y:
                    boss_bullets.append(boss_bullet_class(round(boss.x + 25), round(boss.y + 25), 10, (255,0,0), 0,1))
                else:
                    boss_bullets.append(boss_bullet_class(round(boss.x + 25), round(boss.y + 25), 10, (255,0,0), 0,-1))
            elif abs(boss.y - player.rect.y) < 40:
                if boss.x < player.rect.x:
                    boss_bullets.append(boss_bullet_class(round(boss.x + 25), round(boss.y + 25), 10, (255,0,0), 1,0))
                else:
                    boss_bullets.append(boss_bullet_class(round(boss.x + 25), round(boss.y + 25), 10, (255,0,0), -1,0))
            else:
                #diagonala
                if boss.x < player.rect.x and boss.y < player.rect.y:
                    boss_bullets.append(boss_bullet_class(round(boss.x + 25), round(boss.y + 25), 10, (255,0,0), 1,1))
                if boss.x > player.rect.x and boss.y < player.rect.y:
                    boss_bullets.append(boss_bullet_class(round(boss.x + 25), round(boss.y + 25), 10, (255,0,0), -1,1))
                if boss.x < player.rect.x and boss.y > player.rect.y:
                    boss_bullets.append(boss_bullet_class(round(boss.x + 25), round(boss.y + 25), 10, (255,0,0), 1,-1))
                if boss.x > player.rect.x and boss.y > player.rect.y:
                    boss_bullets.append(boss_bullet_class(round(boss.x + 25), round(boss.y + 25), 10, (255,0,0), -1,-1))

def handle_boss_bullets_logic(boss_bullets, player, rd,game_map,normal_bullets):
    #gloantele trase merg putin si apoi se impart in 4
    for bullet in boss_bullets:
            #if bullet.facing == 1 or bullet.facing == -1:
            if (abs(bullet.x - rd.x) < 100 and abs(bullet.y - rd.y) < 100):
                bullet.x += 2 * bullet.velx
                bullet.y += 2 * bullet.vely
            else:
                normal_bullets.append(bullet_class(round(bullet.x), round(bullet.y), 8, (255,0,0), 1,1,0))
                normal_bullets.append(bullet_class(round(bullet.x), round(bullet.y), 8, (255,0,0), -1,1,0))
                normal_bullets.append(bullet_class(round(bullet.x), round(bullet.y), 8, (255,0,0), 0,1,-1))
                normal_bullets.append(bullet_class(round(bullet.x), round(bullet.y), 8, (255,0,0), 0,1,1))
                boss_bullets.pop(boss_bullets.index(bullet))
            if overlap(player.rect.x + 16,player.rect.y + 16,31,bullet.x,bullet.y,bullet.radius):
                boss_bullets.pop(boss_bullets.index(bullet))
                player.take_damage(34)
            else:
                for i in range(len(game_map.walls)):
                    if overlap(game_map.walls[i].x + 25,game_map.walls[i].y + 25,50,bullet.x,bullet.y,bullet.radius):
                        normal_bullets.append(bullet_class(round(bullet.x), round(bullet.y), 8, (255,0,0), 1,1,0))
                        normal_bullets.append(bullet_class(round(bullet.x), round(bullet.y), 8, (255,0,0), -1,1,0))
                        normal_bullets.append(bullet_class(round(bullet.x), round(bullet.y), 8, (255,0,0), 0,1,-1))
                        normal_bullets.append(bullet_class(round(bullet.x), round(bullet.y), 8, (255,0,0), 0,1,1))
                        boss_bullets.pop(boss_bullets.index(bullet))
                        break

def handle_split_bullets_logic(split_bullets, player,game_map):
    #gloantele impartite sunt asemanatoare cu gloantele normale, doar ca dau mai mult damage
    for bullet in split_bullets:
            vf = 0
            if bullet.velx != 0:
                if abs(bullet.x - bullet.startx) < 1000:
                    bullet.x += 2 * bullet.velx
                else:
                    vf = 1
                    split_bullets.pop(split_bullets.index(bullet))
            if bullet.vely != 0:
                if abs(bullet.y - bullet.starty) < 1000:
                    bullet.y += 2 * bullet.vely
                else:
                    vf = 0
                    split_bullets.pop(split_bullets.index(bullet))
            if overlap(player.rect.x + 16,player.rect.y + 16,32,bullet.x,bullet.y,bullet.radius) and vf == 0:
                split_bullets.pop(split_bullets.index(bullet))
                player.take_damage(25)
            else:
                for i in range(len(game_map.walls)):
                    if overlap(game_map.walls[i].x + 25,game_map.walls[i].y + 25,50,bullet.x,bullet.y,bullet.radius) and vf == 0:
                        split_bullets.pop(split_bullets.index(bullet))
                        break
