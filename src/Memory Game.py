
import pygame
from pygame.locals import *
import random
from turtle import screensize

class MemoryGame:

    def __init__(self, screensize=(1200,720)):
        pygame.init()
        pygame.display.set_caption("Memory Game")

        self.black, self.white = (0, 0, 0), (255, 255, 255)
        self.screensize = screensize
        self.screenrect = pygame.Rect(0, 0, self.screensize[0], self.screensize[1])
        self.screen = pygame.display.set_mode(self.screensize)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def loop(self):
        self.handle_events()

    def run(self):
        while True:
            self.loop()


if __name__ == '__main__':

    game = MemoryGame()
    game.run()