import pygame, sys
from pygame.locals import *

# width and height
width = 600
height = 600

# color
white = (255, 255, 255)
green = (0, 255, 0)
black = (0, 0, 0)


# anime the ball
def animeBall(ball, dim):
    left = 0
    right = dim

    if ball['ball'].left < left or ball['ball'].right > right:
        ball['vel'][0] = - ball['vel'][0]
    ball['ball'].x += ball['vel'][0]

# anime the rect
def animeRect(fig, pos):
    top = 0
    bottom = pos
    if fig['rect'].top < top or fig['rect'].bottom > bottom:
        fig['vel'][1] = -fig['vel'][1]
    fig['rect'].y += fig['vel'][1]


    if fig['rect'].top < top or fig['rect'].bottom > bottom:
        fig['vel'][1] = -fig['vel'][1]
    fig['rect'].y += fig['vel'][1]

def main():
    pygame.init()

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Animation 4')

    # time for update the screen
    rel = pygame.time.Clock()

    # draw two rect
    rect1 = {'rect':pygame.Rect(10, 250, 20, 150), 'color':white, 'vel':[0, 3]}
    rect2 = {'rect':pygame.Rect(570, 250, 20, 150), 'color':white, 'vel':[0, 3]}

    # draw ball
    ball = {'ball':pygame.Rect(300, 300, 40, 40), 'color':green, 'vel':[6, 0]}

    while True:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, rect1['color'], rect1['rect'])
        pygame.draw.rect(screen, rect2['color'], rect2['rect'])

        # draw and anime the ball
        animeBall(ball, width)
        pygame.draw.rect(screen, ball['color'], ball['ball'])

        collide1 = ball['ball'].colliderect(rect1['rect'])
        collide2 = ball['ball'].colliderect(rect2['rect'])
        if collide1:
            ball['vel'] = [6, 0]
        elif collide2:
            ball['vel'] = [-6, 0]

        pygame.display.update()
        rel.tick(40)

if __name__ == '__main__':
    main()

