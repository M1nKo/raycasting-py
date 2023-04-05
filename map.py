#Este archivo contendrá todo lo relativo al mapeado del juego
import pygame as pg

_ = False
# 1 = pared
# _ = hueco
mini_map = [
    [_, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [_, _, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, 1],
    [_, _, _, _, _, _, _, _, _, _, _, 1, _, 1, 1, 1],
    [_, _, _, 1, 1, 1, 1, 1, 1, 1, _, 1, _, 1, 1, 1],
    [_, _, _, 1, 1, 1, 1, 1, 1, 1, _, 1, _, 1, 1, 1],
    [_, _, _, 1, 1, 1, 1, 1, 1, 1, _, 1, _, 1, 1, 1],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, 1, 1, 1],
    [_, _, _, _, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i,j)] = value

    #dibuja nuestro mapa a partir de la matriz
    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]