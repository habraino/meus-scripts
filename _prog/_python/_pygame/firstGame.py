import pygame
import sys
from random import randint
from pygame.locals import *
from time import sleep

# width and height of window of game
WIDTH = 500
HEIGHT = 400

# weight of screen
W = 750
H = 500

# SOME COLORS
BACKGROUD = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (11, 105, 255)
GREY = (179, 179, 179)
GREEN_LIGHT = (170, 212, 0)
ROSE = (255, 43, 233)
ORANGE = (170, 88, 0)
VIOLET = (136, 0, 170)


# another variables
rel = pygame.time.Clock()
VEL = 6
key = {'left':False, 'right':False}
ball_posX = 270
ball_posY = 320
player_posX = 270
player_posY = 360
cont = 0
posX = 0
posY = 0
interplay = 10
sizeBlock = 10
block = list()
contCollaps = 0

# rule to mouve box
def mouveBlock(block):
    block['rect'].y += block['vel']

# rule of moviment of ball
def moveBall(figure, weight):
    left = 0
    top = 0
    right = weight[0]
    bottom = weight[1]

    if figure['rect'].top < top or figure['rect'].bottom > bottom:
        figure['vel'][1] = -figure['vel'][1]
    if figure['rect'].left < left or figure['rect'].right > right:
        figure['vel'][0] = -figure['vel'][0]
    figure['rect'].x += figure['vel'][0]
    figure['rect'].y += figure['vel'][1]

# create method of mouve player
def mouvePlayer(figure, key, weight):
    left = 0
    right = weight

    if key['left'] and figure['rect'].left > left:
        figure['rect'].x -= figure['vel']
    if key['right'] and figure['rect'].right < right:
        figure['rect'].x += figure['vel']

# create new order figures
def createFigure(figures):
    # create figures
    for figure in figures:
        pygame.draw.rect(screen, figure['color'], figure['rect'])

# define position initial of player and ball
def positionStart():
    ball['rect'].x = ball_posX
    ball['rect'].y = ball_posY
    player['rect'].x = player_posX
    player['rect'].y = player_posY

# method case player win the game
def youLose():
    pygame.mixer.music.load("somErro.wav")
    pygame.mixer.music.play(1)
    figures.clear()
    figures.extend(figureCopy)  # pass the copy of list

# method case player win the game:
def newGame():
    figures.clear()
    figures.extend(figureCopy)  # pass the copy of list
    createFigure(figures)


# init pygame
pygame.init()

# create new screen
main_screen = pygame.display.set_mode((W, H))
screen = pygame.Surface((WIDTH, HEIGHT))
pygame.display.set_caption('MY FIRST GAME')


# create figures
f1 = {'rect':pygame.Rect(20, 20, 100, 20), 'color':YELLOW}
f2 = {'rect':pygame.Rect(140, 20, 100, 20), 'color':GREEN}
f3 = {'rect':pygame.Rect(260, 20, 100, 20), 'color':BLUE}
f4 = {'rect':pygame.Rect(380, 20, 100, 20), 'color':WHITE}
f5 = {'rect':pygame.Rect(20, 50, 100, 20), 'color':VIOLET}
f6 = {'rect':pygame.Rect(140, 50, 100, 20), 'color':ROSE}
f7 = {'rect':pygame.Rect(260, 50, 100, 20), 'color':YELLOW}
f8 = {'rect':pygame.Rect(380, 50, 100, 20), 'color':GREEN}
f9 = {'rect':pygame.Rect(20, 80, 100, 20), 'color':WHITE}
f10 = {'rect':pygame.Rect(140, 80, 100, 20), 'color':YELLOW}
f11 = {'rect':pygame.Rect(260, 80, 100, 20), 'color':GREEN_LIGHT}
f12 = {'rect':pygame.Rect(380, 80, 100, 20), 'color':ORANGE}
f13 = {'rect':pygame.Rect(20, 110, 100, 20), 'color':ROSE}
f14 = {'rect':pygame.Rect(140, 110, 100, 20), 'color':VIOLET}
f15 = {'rect':pygame.Rect(260, 110, 100, 20), 'color':BLUE}
f16 = {'rect':pygame.Rect(380, 110, 100, 20), 'color':WHITE}
f17 = {'rect':pygame.Rect(20, 140, 100, 20), 'color':GREEN}
f18 = {'rect':pygame.Rect(140, 140, 100, 20), 'color':ORANGE}
f19 = {'rect':pygame.Rect(260, 140, 100, 20), 'color':GREEN_LIGHT}
f20 = {'rect':pygame.Rect(380, 140, 100, 20), 'color':VIOLET}

# put all figures in list
figures = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20]
figureCopy = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20]

# create the ball
ball = {'rect':pygame.Rect(270, 320, 30, 30), 'color':RED, 'vel':[2, 2]}

# crate player
player = {'rect':pygame.Rect(270, 360, 100, 20), 'color':GREY, 'vel':VEL}

# create the of points
font = pygame.font.Font(None, 50)

#imgage
img = pygame.image.load("coin.png")
contCoin = 0

# som of game
som = pygame.mixer.Sound("SomFundo.ogg")

# main game loop
while True:
    # verify the events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # event of moviment of player
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                key['left'] = True
            if event.key == K_RIGHT:
                key['right'] = True
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                key['left'] = False
            if event.key == K_RIGHT:
                key['right'] = False

    # making the animation
    cont += 1
    if cont >= interplay:
        # adding new block
        cont = 0
        posX = randint(0, (WIDTH - sizeBlock))
        posY = sizeBlock
        velRandom = randint(1, VEL + 2)
        block.append({'rect': pygame.Rect(posX, posY, sizeBlock, sizeBlock), 'color': WHITE, 'vel': velRandom})

    # moving and draw the blocks
    for bl in block:
        mouveBlock(bl)
        pygame.draw.ellipse(screen, bl['color'], bl['rect'])

    # verify conllision with figures
    for figure in figures[:]:
        colideFig = ball['rect'].colliderect(figure['rect'])
        if colideFig or ball['rect'].y > HEIGHT:
            pygame.mixer.music.load("somColide.wav")
            pygame.mixer.music.play(1)
            ball['vel'] = [-3, 3]
            figures.remove(figure)
            contCollaps += 1

    # start the game
    if len(figures) > 0 and ball['rect'].y < player['rect'].y:
        createFigure(figures)
    else:
        if ball['rect'].y >= player['rect'].y: # if player lose
            contCollaps = 0
            contCoin = 0
            youLose()
            som.stop()
            sleep(3)
            positionStart()
            createFigure(figures)
        elif len(figures) <= 0 and ball['rect'].y < player['rect'].y:
            som.stop()
            pygame.mixer.music.load("aplausos.ogg")
            pygame.mixer.music.play(1)
            sleep(3)
            pygame.mixer.music.stop()
            positionStart()
            newGame()
            contCoin += 1


    # test collision between player and ball
    colidPlayer = player['rect'].colliderect(ball['rect'])
    if colidPlayer:
        ball['vel'][1] = -ball['vel'][1]
        ball['rect'].y += ball['vel'][1]

    # moving and create the ball
    moveBall(ball, (WIDTH, HEIGHT))
    pygame.draw.ellipse(screen, ball['color'], ball['rect'])

    # movendo e create the player
    mouvePlayer(player, key, WIDTH)
    pygame.draw.rect(screen, player['color'], player['rect'], 1)


    # fill the background in black
    main_screen.fill(WHITE)
    main_screen.blit(screen, [20, 20]) # put the surface of game in main_screen
    text = font.render("Point: "+str(contCollaps), True, RED, WHITE)
    main_screen.blit(text, [530, 30]) # put the text in screen
    textCoin = font.render("Coin: "+str(contCoin), True, GREEN, WHITE)
    main_screen.blit(textCoin, [530, 80])
    main_screen.blit(img, [650, 80])
    screen.fill(BACKGROUD)

    rand_col = (randint(0, 255), randint(0, 255), randint(0, 255))
    for _ in range(100):
        rand_pos = (randint(0, 639), randint(0, 479))
        screen.set_at(rand_pos, rand_col)

    # play the sound
    som.play(1)

    # update the game
    pygame.display.update()

    rel.tick(70)

