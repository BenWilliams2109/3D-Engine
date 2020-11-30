from pygame.locals import *
import pygame
import keyboard
import os
import math
import time
import sys

pygame.init()

os.environ["SDL_VIDEO_CENTERED"] = '1'
black, white, blue, green, red = (20, 20, 20), (230, 230, 230), (0, 154, 255), (0, 201, 87), (238, 59, 59)
width, height = 1440, 1080
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


class Player:

    def __init__(self, px, py, angle, vx1, vx2, vy1, vy2):

        self.downW = False
        self.downS = False
        self.downD = False
        self.downA = False

        self.px = px
        self.py = py
        self.angle = angle
        self.vx1 = vx1
        self.vx2 = vx2
        self.vy1 = vy1
        self.vy2 = vy2

    def Key_Presses(self):

        game_over = False

        while not game_over:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    game_over = True

                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    self.downW = True
                elif event.type == pygame.KEYUP and event.key == pygame.K_s:
                    self.downW = False

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                    self.downS = True
                elif event.type == pygame.KEYUP and event.key == pygame.K_w:
                    self.downS = False

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    self.downA = True
                elif event.type == pygame.KEYUP and event.key == pygame.K_a:
                    self.downA = False

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    self.downD = True
                elif event.type == pygame.KEYUP and event.key == pygame.K_d:
                    self.downD = False

            if self.downW:
                self.px += math.cos(self.angle) * 10
                self.py += math.sin(self.angle) * 10
            if self.downS:
                self.px -= math.cos(self.angle) * 10
                self.py -= math.sin(self.angle) * 10
            if self.downD:
                self.angle += 0.01
            if self.downA:
                self.angle -= 0.01

            tx1 = (self.vx1 - self.px) * math.sin(self.angle) - (self.vy1 - self.py) * math.cos(self.angle)
            tx2 = (self.vx2 - self.px) * math.sin(self.angle) - (self.vy2 - self.py) * math.cos(self.angle)

            tz1 = (self.vx1 - self.px) * math.cos(self.angle) + (self.vy1 - self.py) * math.sin(self.angle)
            tz2 = (self.vx2 - self.px) * math.cos(self.angle) + (self.vy2 - self.py) * math.sin(self.angle)

            x1 = -tx1 * 16/ tz1
            x2 = -tx2 * 16/ tz2

            y1a = 240 / tz1
            y2a = 240 / tz2

            y1b = 840 / tz1
            y2b = 840 / tz2

            time.sleep(0.03)
            screen.fill(black)
            pygame.display.set_caption("Work in Progress")

            pygame.draw.line(screen, blue, ((740 + x1), (540 + y1a)), ((740 + x2), (540 + y2a)), 3)
            pygame.draw.line(screen, red, ((740 + x1), (540 + y1b)), ((740 + x2), (540 + y2b)), 3)
            pygame.draw.line(screen, green, ((740 + x1), (540 + y1a)), ((740 + x1), (540 + y1b)), 3)
            pygame.draw.line(screen, white, ((740 + x2), (540 + y2a)), ((740 + x2), (540 + y2b)), 3)

            pygame.display.update()


p1 = Player(720, 540, 0, 240, 240, 150, 900)
p1.Key_Presses()
pygame.quit()
