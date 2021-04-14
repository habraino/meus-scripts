import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()
screen = pygame.display.set_mode((500, 400), 0, 32)

black = pygame.Color(0, 0, 0)

for _ in range(25):
    rand_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    rand_pos = (randint(0, 639), randint(0, 479))
    rand_radius = (randint(0, 100))
    pygame.draw.circle(screen, rand_color, rand_pos, rand_radius)
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    screen.fill(black)


