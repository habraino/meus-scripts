import pygame
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Font Example')

# colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GREEN = (0, 155, 0)

screen.fill(WHITE)  # set color to backgroung

# darw in screen
pygame.draw.polygon(screen, BLUE, ((191, 206), (236, 277), (150, 277)), 0)
pygame.draw.line(screen, GREEN, (150, 360), (350, 360), 20)
pygame.draw.circle(screen, RED, (250, 330), 20, 0)
pygame.draw.ellipse(screen, BLACK, (40, 200, 60, 100), 2)
pygame.draw.rect(screen, BLUE, (320, 150, 150, 50), 20)

# make texts
font = pygame.font.Font(None, 50)
text1 = font.render('Hello World', True, WHITE, RED)
text2 = font.render('Coding in Pygame!', True, YELLOW, BLACK)

screen.blit(text1, [150, 50])  # set text to screen
screen.blit(text2, [80, 100])  # here so set text to screen

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()


