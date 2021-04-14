import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30# frame per second settings
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 500), 20, 10)
pygame.display.set_caption('Animation Example')

WHITE = (255, 255, 255)
screen.fill(WHITE)

img = pygame.image.load("images.png")
imgX = 10
imgY = 10

diretion = 'right'

while True:

    if diretion == 'right':
        imgX += 5
        if imgX == 360:
            diretion = 'down'
    elif diretion == 'down':
        imgY += 5
        if imgY == 220:
            diretion = 'left'
    elif diretion == 'left':
        imgX -= 5
        if imgX == 10:
            diretion = 'up'
    elif diretion == 'up':
        imgY -= 5
        if imgY == 10:
            diretion = 'right'

    screen.blit(img, (imgX, imgY))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

    fpsClock.tick(FPS)
