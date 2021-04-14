import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600, 500))
title = 'First program in Pygame'
pygame.display.set_caption(title)

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((20, 150, 60)) # set a backgroundcolor to screen
    pygame.Rect(10, 20, 200, 300)
    pygame.display.update()

