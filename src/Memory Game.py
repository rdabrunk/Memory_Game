import numpy as np
import pygame
from time import sleep
from pygame.locals import *
import random
from turtle import screensize
import numpy

class MemoryGame:

    def __init__(self, screensize=(1200,720)):
        pygame.init()
        pygame.display.set_caption("Memory Game")

        self.black, self.white, self.blue, self.red = (0, 0, 0), (255, 255, 255), (0, 0, 255), (255, 0, 0)
        self.screensize = screensize
        self.screenrect = pygame.Rect(0, 0, self.screensize[0], self.screensize[1])
        self.screen = pygame.display.set_mode(self.screensize)
        self.get_coordinates()
        self.draw_squares()
        pygame.display.update()
        self.draw_round(5)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            

    def get_coordinates(self):
        self.x_positions = np.linspace(self.screensize[0] * 0.15 ,self.screensize[0] * 0.8, 4)
        self.y_positions = np.linspace(self.screensize[1] * 0.2, self.screensize[1] * 0.8, 4)


    def draw_squares(self):
        for i in range(4):
            for j in range(4):
                pygame.draw.rect(self.screen, self.blue, (self.x_positions[i], self.y_positions[j], 60,60))

    def draw_red_square(self):
        x_index = random.randrange(4)
        y_index = random.randrange(4)
        pygame.draw.rect(self.screen, self.red, (self.x_positions[x_index], self.y_positions[y_index], 60,60))


    def draw_round(self, num_range):
        for i in range(num_range):
            sleep(0.5)
            self.draw_squares()
            self.draw_red_square()
            pygame.display.update()
            sleep(0.5)
        sleep(0.5)
        self.draw_squares()

    def loop(self):
        self.handle_events()
        pygame.display.update()

    def run(self):
        while True:
            self.loop()


if __name__ == '__main__':

    game = MemoryGame()
    game.run()