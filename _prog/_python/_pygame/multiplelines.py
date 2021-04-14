import sys, pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500, 600), 0, 32)

points = list()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEMOTION:
            points.append(event.pos)
            if len(points) > 100:
                del points[0]
    screen.fill((255, 255, 255))

    if len(points) > 1:
        pygame.draw.lines(screen, (0, 255, 0), False, points, 2)

    pygame.display.update()

