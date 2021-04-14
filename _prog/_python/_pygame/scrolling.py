from pygame.locals import *
import pygame, sys

pygame.init()

SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE)

text = "  PYGAME IS VERY EASY... "
font = pygame.font.SysFont('arial', 80)
text_surface = font.render(text, True, (0, 0, 255))
x = 0
y = 196

while True:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    x -= 2
    if x < -1019:
        x = 0

    screen.blit(text_surface, (x, y))
    screen.blit(text_surface, (x+1019, y))

    pygame.display.update()
