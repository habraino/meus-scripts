from pygame.locals import *
import pygame, sys

pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

font = pygame.font.SysFont('arial', 60)
text = font.render("Pygame Test", True, (0, 255, 0))

img = pygame.image.load('init_game.png').convert()

while True:

    screen.blit(text, (300, 500))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == VIDEORESIZE:
            SCREEN_SIZE = event.size
            screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
            pygame.display.set_caption("Window resized to " + str(event.size))

    screen_width, screen_height = SCREEN_SIZE

    for x in range(0, screen_height, img.get_height()):
        for y in range(0, screen_width, img.get_width()):
            screen.blit(img, (x, y))


    pygame.display.update()



