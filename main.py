import pygame
from pygame.locals import *
import pygame.freetype

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

#text - main menu
def maintext(running, defaultText = 'Press "=" to run the game'):
    if running == 1:
        font = pygame.font.SysFont(None, 60)
        img = font.render(defaultText, True, BLUE)
        pygame.display.update()      
        screen.blit(img, (500, 360))

#player - controls | not yet done 
def playerMovement():
    if event.key == pygame.K_r:
        Background = RED
        screen.fill(Background)
        pygame.display.update()
    if event.key == pygame.K_g:
        Background = GREEN
        screen.fill(Background)
        pygame.display.update()
    if event.key == pygame.K_b:
        Background = BLUE
        screen.fill(Background)
        pygame.display.update() 
    

running = True
while running:
    for event in pygame.event.get():
        maintext(1)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            #Player movement - controls
            playerMovement()
            if event.key == pygame.K_EQUALS:
                pygame.display.update()
                screen.fill(pygame.Color("black")) # erases the entire screen surface
                maintext(0, 'Game is running')
                screen.blit(screen, (0, 0))
                print("Start")

pygame.quit()

