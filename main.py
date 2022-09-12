import pygame
from pygame.locals import *
import pygame.freetype

pygame.init()

#Define simple colors
screen = pygame.display.set_mode((1280, 720));

#set default colors
bgColor = (51, 51, 51)
textColor = (255, 255, 255)

# default background
screen.fill(bgColor)
pygame.display.update()

#game state
game = 1
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = 0
        if event.type == pygame.KEYDOWN:
            #Player movement - controls
            if event.key == pygame.K_EQUALS:
                print("pressed =")

pygame.quit()