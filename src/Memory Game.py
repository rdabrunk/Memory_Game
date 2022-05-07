import numpy as np
import pygame
from pygame.locals import *
import random
from turtle import screensize
import numpy

class MemoryGame:

    def __init__(self, screensize=(1200,720)):
        pygame.init()
        pygame.display.set_caption("Memory Game")

        self.black, self.white, self.blue = (0, 0, 0), (255, 255, 255), (0, 0, 255)
        self.screensize = screensize
        self.screenrect = pygame.Rect(0, 0, self.screensize[0], self.screensize[1])
        self.screen = pygame.display.set_mode(self.screensize)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def draw_squares(self):
        square_x_positions = np.linspace(self.screensize[0] * 0.15 ,self.screensize[0] * 0.8, 4)
        square_y_positions = np.linspace(self.screensize[1] * 0.2, self.screensize[1] * 0.8, 4)
        for i in range(4):
            for j in range(4):
                pygame.draw.rect(self.screen, self.blue, (square_x_positions[i], square_y_positions[j], 60,60))

    def loop(self):
        self.handle_events()
        self.draw_squares()
        pygame.display.update()

    def run(self):
        while True:
            self.loop()


if __name__ == '__main__':

    game = MemoryGame()
    game.run()