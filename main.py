import pygame
from pygame.locals import *


pygame.init()
#Define simple colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
screen = pygame.display.set_mode((1280, 720));
#set default background
Background = GREEN;
screen.fill(Background)
pygame.display.update()
# Simple way of quitting an event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                Background = BLUE
                screen.fill(Background)
                pygame.display.update()
pygame.quit()

