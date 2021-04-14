from pygame.locals import *
import pygame, sys

pygame.init()

screen = pygame.display.set_mode((640, 480))

# creates images with smooth gradients
def create_scale(height):
    red_scale_surface = pygame.Surface((640, height))
    green_scale_surface = pygame.Surface((640, height))
    blue_scale_surface = pygame.Surface((640, height))

    for x in range(640):
        c = int((x/639.)*255.)
        red = (c, 0, 0)
        green = (0, c, 0)
        blue = (0, 0, c)
        line_rect = Rect(x, 0, 1, height)
        pygame.draw.rect(red_scale_surface, red, line_rect)
        pygame.draw.rect(green_scale_surface, green, line_rect)
        pygame.draw.rect(blue_scale_surface, blue, line_rect)

    return red_scale_surface, green_scale_surface, blue_scale_surface

red_scale, green_scale, blue_scale = create_scale(80)
color = [127, 127, 127]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    screen.fill((0, 0, 0))

    # Draw the scales to the screen
    screen.blit(red_scale, (0, 00))
    screen.blit(green_scale, (0, 80))
    screen.blit(blue_scale, (0, 160))


    x, y = pygame.mouse.get_pos()

    # If the mouse was pressed on one of the sliders, adjust the color component
    if pygame.mouse.get_pressed()[0]:
        for c in range(3):
            if y > c * 80 and y < (c + 1) * 80:
                color[c] = int((x/639.)*255.)
                pygame.display.set_caption("PyGame Color Test - " + str(tuple(color)))

    # Draw a circle for each slider to represent the current setting
    for c in range(3):
        pos = (int((color[c]/255.)*639), c * 80 + 40)
        pygame.draw.circle(screen, (255, 255, 255), pos, 4)

    pygame.draw.rect(screen, tuple(color), (0, 240, 640, 240))

    pygame.display.update()




