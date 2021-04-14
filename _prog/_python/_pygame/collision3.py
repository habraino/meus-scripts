import pygame, sys
from pygame.locals import *

# método para criar movimento dos elementos na tela
def mover(figura, dimessao):
    esquerda = 0
    cima = 0
    direita = dimessao[0]
    baixo = dimessao[1]

    if figura['rect'].top < cima or figura['rect'].bottom > baixo:
        figura['vel'][1] = -figura['vel'][1]
    if figura['rect'].left < esquerda or figura['rect'].right > direita:
        figura['vel'][0] = -figura['vel'][0]
    figura['rect'].x += figura['vel'][0]
    figura['rect'].y += figura['vel'][1]


# inicia os módulos do pygame
pygame.init()

# criando um objeto pygame.time.Clock
relogio = pygame.time.Clock()

# dimensão da tela
largura = 500
altura = 400

# cores
verde = (0, 255, 0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
amarela = (255, 255, 0)
rosa = (255, 0, 255)
preto = (0, 0, 0)
branco = (255, 255, 255)

# cria figuras
f1 = {'rect':pygame.Rect(375, 80, 40, 40), 'cor':azul, 'vel': [0,2]}
f2 = {'rect':pygame.Rect(175, 200, 40, 40), 'cor':verde, 'vel': [0,-3]}
f3 = {'rect':pygame.Rect(275, 150, 40, 40), 'cor':amarela, 'vel': [0,-1]}
f4 = {'rect':pygame.Rect(75, 150, 40, 40), 'cor':rosa, 'vel': [0,4]}

figuras = [f1, f2, f3, f4] # cria uma lista com figuras

# criando a bola
bola = {'rect': pygame.Rect(270, 330, 30, 30), 'cor': branco, 'vel': [3,3]}

# tratamento da tela
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Exemplo de Animação Colisão')

while True:
    # a cor do fundo fica preto
    janela.fill(preto)

    # verifica os possíveis eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for figura in figuras:
        mover(figura, (largura, altura))
        pygame.draw.rect(janela, figura['cor'], figura['rect'])

        # pega colisão e armazena na variável
        colide = bola['rect'].colliderect(figura['rect'])
        if colide: # se houver colisão
            bola['cor'] = figura['cor'] # pega a cor o objecto colidido

    # reposicionando e desenha a bola
    mover(bola, (largura, altura))
    pygame.draw.ellipse(janela, bola['cor'], bola['rect'])

    pygame.display.update()
    relogio.tick(50)

