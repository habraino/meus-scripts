import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 50
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Movendo a Bola')

RED = (255, 0, 0)
WHITE = (255, 255, 255)

screen.fill(WHITE)
bola = pygame.image.load("bola.png")

bolaX = 10
bolaY = 10

diretion = 'right'

while True:
    if diretion == 'right':
        bolaX += 5
        if bolaX == 420:
            diretion = 'down'
    elif diretion == 'down':
        bolaY += 5
        if bolaY == 320:
            diretion = 'left'
    elif diretion == 'left':
        bolaX -= 5
        if bolaX == 10:
            diretion = 'up'
    elif diretion == 'up':
        bolaY -= 5
        if bolaY == 10:
            diretion = 'right'

    screen.blit(bola, (bolaX, bolaY))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

    fpsClock.tick(FPS)

