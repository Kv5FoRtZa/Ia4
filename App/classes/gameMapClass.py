import pygame
from classes.objectClass import Block, Trap
from classes.bossEnemy import boss

class GameMap:
    def __init__(self, layout, tile_size):
        self.layout = layout
        self.tile_size = tile_size
        self.walls = []
        self.traps = []
        self.bosss = []
        self.create_map_objects()

    def create_map_objects(self):
        self.walls = []
        self.traps = []
        self.bosss = []

        # enumerate() -- loops through a list/ tuple/ etc -- you have acces to both the index and the element itself
        for row_idx, row in enumerate(self.layout):
            for col_idx, tile in enumerate(row):

                x = col_idx * self.tile_size
                y = row_idx * self.tile_size

                if tile == 1:
                    self.walls.append(Block(x, y, self.tile_size))
                elif tile == -1:
                    self.traps.append(Trap(x, y, self.tile_size, self.tile_size))
                elif tile == 6:
                    self.bosss.append(boss(x, y, 300,300,300 + 2 * x))
                # alte elemente cand avem

    def draw(self, window):
        for wall in self.walls:
            wall.draw(window)
        for trap in self.traps:
            trap.draw(window)
        for bt in self.bosss:
            bt.draw(window,self.walls)