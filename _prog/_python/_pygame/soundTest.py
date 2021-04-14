import  pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Example with sound')

pygame.mixer.music.load("Calema - Tempo.mp3")
pygame.mixer.music.play(-1, 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()




