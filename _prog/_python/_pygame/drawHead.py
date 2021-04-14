import pygame
from pygame.locals import *
import sys

pygame.init()

screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('Draw 1')

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PI = 3.14159
screen.fill(WHITE)

#draw head of robot in screen
pygame.draw.circle(screen, RED, (300, 150), 100, 0)
pygame.draw.line(screen, GREEN, (230, 130), (260, 130), 10)
pygame.draw.line(screen, GREEN, (320, 130), (350, 130), 10)
pygame.draw.line(screen, YELLOW, (260, 180), (330, 180), 10)
pygame.draw.arc(screen, BLUE, [170, 100, 90, 100], PI/2, 3*PI/2, 5)
pygame.draw.arc(screen, BLUE, [340, 100, 90, 100], -PI/2, PI/2, 5)
pygame.draw.rect(screen, BLACK, (290, 20, 20, 40), 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

