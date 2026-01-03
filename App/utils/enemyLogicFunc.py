import pygame
from classes.overlapClass import *
from classes.bulletClass import bullet_class
from utils.backgroudFunc import *
import sys
from classes.bossBulletClass import *

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
            if game_map.bosss:
                if overlap(game_map.bosss[0].x + game_map.bosss[0].height / 2,game_map.bosss[0].y + game_map.bosss[0].width / 2,game_map.bosss[0].height,bullet.x,bullet.y,bullet.radius):
                    bullets.pop(bullets.index(bullet))
                    game_map.bosss[0].damage()
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
                player.take_damage(20)
            else:
                for i in range(len(game_map.walls)):
                    if overlap(game_map.walls[i].x + 50,game_map.walls[i].y + 50,100,bullet.x,bullet.y,bullet.radius):
                        enemy_bullets.pop(enemy_bullets.index(bullet))
                        break

def handle_boss_bullets_logic(boss_bullets, player, rd,game_map,normal_bullets):
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
            if overlap(player.rect.x + 25,player.rect.y + 25,50,bullet.x,bullet.y,bullet.radius):
                boss_bullets.pop(boss_bullets.index(bullet))
                player.take_damage(34)
            else:
                for i in range(len(game_map.walls)):
                    if overlap(game_map.walls[i].x + 50,game_map.walls[i].y + 50,100,bullet.x,bullet.y,bullet.radius):
                        normal_bullets.append(bullet_class(round(bullet.x), round(bullet.y), 8, (255,0,0), 1,1,0))
                        normal_bullets.append(bullet_class(round(bullet.x), round(bullet.y), 8, (255,0,0), -1,1,0))
                        normal_bullets.append(bullet_class(round(bullet.x), round(bullet.y), 8, (255,0,0), 0,1,-1))
                        normal_bullets.append(bullet_class(round(bullet.x), round(bullet.y), 8, (255,0,0), 0,1,1))
                        boss_bullets.pop(boss_bullets.index(bullet))
                        break

def handle_split_bullets_logic(split_bullets, player,game_map):
    for bullet in split_bullets:
            if bullet.velx != 0:
                if abs(bullet.x - bullet.startx) < 1000:
                    bullet.x += 2 * bullet.velx
                else:
                    split_bullets.pop(split_bullets.index(bullet))
            if bullet.vely != 0:
                if abs(bullet.y - bullet.starty) < 1000:
                    bullet.y += 2 * bullet.vely
                else:
                    split_bullets.pop(split_bullets.index(bullet))
            if overlap(player.rect.x + 25,player.rect.y + 25,50,bullet.x,bullet.y,bullet.radius):
                split_bullets.pop(split_bullets.index(bullet))
                player.take_damage(25)
            else:
                for i in range(len(game_map.walls)):
                    if overlap(game_map.walls[i].x + 50,game_map.walls[i].y + 50,100,bullet.x,bullet.y,bullet.radius):
                        split_bullets.pop(split_bullets.index(bullet))
                        break

def handle_enemy_shooting(rd, enemy_bullets, cnt_tras, nr_rd, rand_X):
    for i in range(len(rd)):
            if (cnt_tras) % int(rand_X[i]) == 0:
                if rd[i].vel >= 0:
                    enemy_bullets.append(bullet_class(round(rd[i].x + 25), round(rd[i].y + 25), 6, (255,0,0), 1,i,0))
                else:
                    enemy_bullets.append(bullet_class(round(rd[i].x + 25), round(rd[i].y + 25), 6, (255,0,0), -1,i,0)) 
def hanle_boss_shooting(boss_bullets, cnt_tras, rand_X,boss,player):
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
