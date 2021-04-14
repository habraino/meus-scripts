import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Drawn Ellipse')


white = (255, 255, 255)
green = (0, 255, 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    screen.fill(white)
    x, y = pygame.mouse.get_pos()
    pygame.draw.ellipse(screen, green, (0, 0, x, y))

    pygame.display.update()



