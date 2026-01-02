import pygame
from classes.overlapClass import *
from classes.bulletClass import bullet_class
from utils.backgroudFunc import *
import sys

def handle_player_bullets_logic(bullets, player, rd, nr_rd,game_map):
    for bullet in bullets:
            if bullet.facing == 1 or bullet.facing == -1:
                if abs(bullet.x - player.rect.x) < 1000:
                    bullet.x += 2 * bullet.vel
                else:
                    bullets.pop(bullets.index(bullet))  
            vf = 0
            for i in range(len(rd)):
                if overlap(rd[i].x + 32,rd[i].y + 32,64,bullet.x,bullet.y,bullet.radius):
                    bullets.pop(bullets.index(bullet))
                    rd[i].damage()
                    vf = 1
            #print(sys.getsizeof(game_map.walls))
            if vf == 0:
                for i in range(len(game_map.walls)):
                    if overlap(game_map.walls[i].x + 50,game_map.walls[i].y + 50,100,bullet.x,bullet.y,bullet.radius):
                        bullets.pop(bullets.index(bullet))
                        break

def handle_enemy_bullets_logic(enemy_bullets, player, rd,game_map):
    for bullet in enemy_bullets:
            if bullet.facing == 1 or bullet.facing == -1:
                if abs(bullet.x - rd[bullet.nr_inamic].x) < 1000:
                    bullet.x += 2 * bullet.vel
                else:
                    enemy_bullets.pop(enemy_bullets.index(bullet))
            if overlap(player.rect.x + 25,player.rect.y + 25,50,bullet.x,bullet.y,bullet.radius):
                enemy_bullets.pop(enemy_bullets.index(bullet))
                player.take_damage(10)
            else:
                for i in range(len(game_map.walls)):
                    if overlap(game_map.walls[i].x + 50,game_map.walls[i].y + 50,100,bullet.x,bullet.y,bullet.radius):
                        enemy_bullets.pop(enemy_bullets.index(bullet))
                        break

def handle_enemy_shooting(rd, enemy_bullets, cnt_tras, nr_rd, rand_X):
    for i in range(len(rd)):
            if (cnt_tras) % int(rand_X[i]) == 0:
                if rd[i].vel >= 0:
                    enemy_bullets.append(bullet_class(round(rd[i].x + 25), round(rd[i].y + 25), 6, (255,0,0), 1,i))
                else:
                    enemy_bullets.append(bullet_class(round(rd[i].x + 25), round(rd[i].y + 25), 6, (255,0,0), -1,i)) 