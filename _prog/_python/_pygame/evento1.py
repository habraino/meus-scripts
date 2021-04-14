from pygame.locals import *
import pygame, sys

pygame.init()

cor_fundo = (255, 255, 255)

janela = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Movendo através das teclas')

img = pygame.image.load('person2.png')
posX, posY = 0, 0
x, y = 0, 0


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                posX = -10
            if event.key == K_RIGHT:
                posX = 10

            if event.key == K_UP:
                posY = -10
            if event.key == K_DOWN:
                posY = 10

        if event.type == KEYUP:
            if event.key == K_LEFT:
                posX = 0
            if event.key == K_RIGHT:
                posX = 0

            if event.key == K_UP:
                posY = 0
            if event.key == K_DOWN:
                posY = 0

        x += posX
        y += posY

        janela.fill(cor_fundo)
        janela.blit(img, (x, y))

        pygame.display.update()



