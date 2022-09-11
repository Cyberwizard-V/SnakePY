import pygame
from pygame.locals import *
import pygame.freetype

pygame.init()
#Define simple colors
screen = pygame.display.set_mode((1280, 720));
#set default bgColor
bgColor = (51, 51, 51)
textColor = (255, 255, 255)

# Simple way of quitting an event loop

#text - main menu
def maintext(running, defaultText = 'Press "=" to run the game'):
    if running == 1:
        font = pygame.font.SysFont(None, 60)
        img = font.render(defaultText, True, textColor)
        pygame.display.update()      
        screen.blit(img, (500, 360))
    else:
        pygame.display.update()
        screen.fill(bgColor)
        pygame.display.update()

#player - controls | not yet done 
def playerMovement():
    if event.key == pygame.K_w:
        screen.fill(bgColor)
        pygame.display.update()
    if event.key == pygame.K_a:
        screen.fill(bgColor)
        pygame.display.update()
    if event.key == pygame.K_s:
        screen.fill(bgColor)
        pygame.display.update()
    if event.key == pygame.K_d:
        screen.fill(bgColor)
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
                maintext(0)
                screen.fill(pygame.Color("black")) # erases the entire screen surface
                maintext(0, 'Game is running')

pygame.quit()