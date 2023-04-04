#Este archivo contendrá las funciones principales del juego

import pygame as pg
import sys
from settings import *
from map import *
from player import *

class Game: 
    def __init__(self):
        pg.init() #iniciamos pygame
        self.screen = pg.display.set_mode(RES) #definimos la resolución de pantalla
        self.clock = pg.time.Clock()
        self.delta_time = 1 #deltaTime = tiempo que ha pasado desde el último frame
        self.new_game()


    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)


    #Método que nos irá actualizando la pantalla
    def update(self):
        self.player.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}') #nos mostrará los fps en pantalla

    #en cada iteración nos pintará la pantalla de negro
    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()


    #checkea las teclas pulsadas
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exist()

    #método con el loop principal del juego
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

#Creamos la instancia del juego y llamamos al método run
if __name__ == '__main__':
    game = Game()
    game.run()