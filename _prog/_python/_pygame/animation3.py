import pygame, sys, time
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1200, 768))
pygame.display.set_caption('Animation 3')

img = pygame.image.load("tart1.jpg")
img2 = pygame.image.load("tart4.jpg")
obj = pygame.image.load("flower.png")

imgX = 10
imgY = 500

diretion = 'right'
white = (255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if diretion == 'right':
        imgX += 5
        if imgX == 760:
            diretion = 'left'
    elif diretion == 'left':
        imgX -= 5
        if imgX == 10:
            diretion = 'right'


    screen.fill(white)

    if diretion == 'right':
        screen.blit(img, (imgX, imgY))
        screen.blit(obj, (980, 570))
    else:
        screen.blit(img2, (imgX, imgY))
        screen.blit(obj, (980, 570))

    time.sleep(0.001)
    pygame.display.update()


