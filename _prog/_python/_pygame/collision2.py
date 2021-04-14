import pygame, sys, time
from pygame.locals import *

pygame.init()

largura = 500
altura = 400

# define cores
branca = (255, 255, 255)
preta = (0, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarela = (255, 255, 0)

def mover(figura, dimensao):
    esquerda = 0
    cima = 0
    direita = dimensao[0]
    baixo = dimensao[1]

    if figura['rect'].top < cima or figura['rect'].bottom > baixo:
        figura['vel'][1] = -figura['vel'][1]
    if figura['rect'].left < esquerda or figura['rect'].right > direita:
        figura['vel'][0] = -figura['vel'][0]
    figura['rect'].x += figura['vel'][0]
    figura['rect'].y += figura['vel'][1]


screen = pygame.display.set_mode((largura, altura))

# define título
pygame.display.set_caption('Movendo bola')

# cria retacngulo na tela
#f1 = {'rect':pygame.Rect(320, 150, 150, 50), 'cor':verde, 'vel':[2, 2]}

# cria a bola
bola1 = {'rect':pygame.Rect(270, 320, 30, 30), 'cor':azul, 'vel':[3, 3]}
bola2 = {'rect':pygame.Rect(270, 320, 30, 30), 'cor':amarela, 'vel':[2, 3]}
bola3 = {'rect':pygame.Rect(270, 320, 30, 30), 'cor':preta, 'vel':[5, 3]}

bolas = [bola1, bola2, bola3]

while True:
    screen.fill(branca)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    for bl in bolas:
        # muda cor da bola de acordo com posição
        mudaCor1 = bl['rect'].collidepoint(250, 0)
        mudaCor2 = bl['rect'].collidepoint(250, 400)
        mudaCor3 = bl['rect'].collidepoint(0, 300)
        mudaCor4 = bl['rect'].collidepoint(500, 300)

        if mudaCor1:
            bl['cor'] = verde
        elif mudaCor2:
            bl['cor'] = azul
        elif mudaCor3:
            bl['cor'] = preta

        # move e cria nova bola
        mover(bl, (largura, altura))
        pygame.draw.ellipse(screen, bl['cor'], bl['rect'])

    pygame.display.update()

    time.sleep(0.02)



