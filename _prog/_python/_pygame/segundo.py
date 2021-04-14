import pygame, sys
from pygame.locals import *

pygame.init() # incia o jogo

# ecrã
screen = pygame.display.set_mode((500, 400), 0, 32)

# título
pygame.display.set_caption('Draw in the Screen')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# set color to background
screen.fill(WHITE)

# draw on the surface object
pygame.draw.polygon(screen, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277),
                                    (0, 106)))

pygame.draw.line(screen, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(screen, BLUE, (120, 60), (60, 120))
pygame.draw.line(screen, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(screen, BLUE, (300, 350), 40, 0)
pygame.draw.ellipse(screen, RED, (100, 280, 100, 60), 1)
pygame.draw.rect(screen, RED, (300, 100, 150, 30))

pixObj = pygame.PixelArray(screen)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj


while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()