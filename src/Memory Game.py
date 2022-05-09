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

        self.black, self.white, self.blue, self.red, self.green = (0, 0, 0), (255, 255, 255), (0, 0, 255), (255, 0, 0), (0, 255, 0)
        self.screensize = screensize
        self.screenrect = pygame.Rect(0, 0, self.screensize[0], self.screensize[1])
        self.screen = pygame.display.set_mode(self.screensize)
        self.click_position = (-100, -100)
        self.num_range = 1
        self.score = 0
        self.is_new_round = True
        self.get_coordinates()
        self.draw_squares()
        self.update_score()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                self.click_position = pygame.mouse.get_pos()
                self.check_position()


    def get_coordinates(self):
        self.x_positions = np.linspace(self.screensize[0] * 0.15 ,self.screensize[0] * 0.8, 4)
        self.y_positions = np.linspace(self.screensize[1] * 0.2, self.screensize[1] * 0.8, 4)

    def update_score(self):
        pygame.draw.rect(self.screen, self.black, (self.screensize[0] * .465, self.screensize[1] * 0.05, 120, 30))
        pygame.display.update()
        score_string = f"Score: {self.score}"
        rendered_score = pygame.font.SysFont("Avenir", 36).render(score_string, True, self.white)
        self.screen.blit(rendered_score, (self.screensize[0] * 0.465, self.screensize[1] * 0.05))
        pygame.display.update()


    def draw_squares(self):
        for i in range(4):
            for j in range(4):
                pygame.draw.rect(self.screen, self.blue, (self.x_positions[i], self.y_positions[j], 60,60))

    def draw_red_square(self):
        x_index = random.randrange(4)
        y_index = random.randrange(4)
        coordinate = (x_index, y_index)
        pygame.draw.rect(self.screen, self.red, (self.x_positions[x_index], self.y_positions[y_index], 60,60))
        return coordinate


    def draw_round(self, num_range):
        self.coordinates = []
        for i in range(num_range):
            sleep(0.5)
            self.draw_squares()
            self.coordinates.append(self.draw_red_square())
            print(self.coordinates)
            pygame.display.update()
            sleep(0.5)
        sleep(0.5)
        self.draw_squares()
        pygame.display.update()

    def check_position(self):
        # print(self.click_position[0], self.click_position[1])
        # print(self.x_positions[self.coordinates[0][0]], self.y_positions[self.coordinates[0][1]])
        if len(self.coordinates) > 0:
            if (self.x_positions[self.coordinates[0][0]]) <= self.click_position[0] and (self.x_positions[self.coordinates[0][0]] + 60) >= self.click_position[0]:
                if self.y_positions[self.coordinates[0][1]] <= self.click_position[1] and (self.y_positions[self.coordinates[0][1]] + 60) >= self.click_position[1]:
                    pygame.draw.rect(self.screen, self.green, (self.x_positions[self.coordinates[0][0]], self.y_positions[self.coordinates[0][1]], 60,60))
                    self.score += 1
                    self.update_score()
                    sleep(0.1)
                    self.draw_squares()
                    pygame.display.update()
                    print("yes")
                    self.coordinates.remove(self.coordinates[0])
            else:
                print("no")
                pygame.quit()
                exit()
        if len(self.coordinates) == 0:
            self.is_new_round = not self.is_new_round

    def loop(self):
        self.handle_events()
        if self.is_new_round:
            self.is_new_round = not self.is_new_round
            self.draw_round(self.num_range)
            self.num_range += 1



    def run(self):
        while True:
            self.loop()


if __name__ == '__main__':

    game = MemoryGame()
    game.run()