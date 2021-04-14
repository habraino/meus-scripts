import pygame, sys, randonTest
from pygame.locals import *

# dimensão da tela
largura = 600
altura = 500

# outras variáveis
vel = 6
interacoes = 10
tamanhoBloco = 20

# cores
preto = (0, 0, 0)
branco = (255, 255, 255)
verde = (0, 255, 0)

# pega posição atual do jogador
def moverJogador(jogador, tecla, dimensao):
    esquerda = 0
    cima = 0
    direita = dimensao[0]
    baixo = dimensao[1]

    if tecla['esquerda'] and jogador['rect'].left > esquerda:
        jogador['rect'].x -= jogador['vel']
    if tecla['direita'] and jogador['rect'].right < direita:
        jogador['rect'].x += jogador['vel']
    if tecla['cima'] and jogador['rect'].top > cima:
        jogador['rect'].y -= jogador['vel']
    if tecla['baixo'] and jogador['rect'].bottom < baixo:
        jogador['rect'].y += jogador['vel']


# move o bloco
def moveBloco(bloco):
    bloco['rect'].y += bloco['vel']

# inicializando pygame
pygame.init()

relogio = pygame.time.Clock()

# criando janela
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Trabalhando com teclado e mouse')

# criando o jogador
jogador = {'rect':pygame.Rect(300, 100, 50, 50), 'cor': verde, 'vel': vel}

# definindo as direções num dicionário
teclas = {'esquerda':False, 'cima':False, 'direita':False, 'baixo':False}

# inicialisando outras variáveis
contador = 0
contClicks = 0
blocos = list()

# configuração do texto e font
font = pygame.font.Font(None, 50)
texto = font.render(str(contClicks), True, verde, preto)


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


        # quando uma tecla é precionada
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
            if event.key == K_LEFT or event.key == K_a:
                teclas['esquerda'] = True
            if event.key == K_RIGHT or event.key == K_d:
                teclas['direita'] = True
            if event.key == K_UP or event.key == K_w:
                teclas['cima'] = True
            if event.key == K_DOWN or event.key == K_s:
                teclas['baixo'] = True

        # quando uma tecla é solta
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_a:
                teclas['esquerda'] = False
            if event.key == K_RIGHT or event.key == K_d:
                teclas['direita'] = False
            if event.key == K_UP or event.key == K_w:
                teclas['cima'] = False
            if event.key == K_DOWN or event.key == K_s:
                teclas['baixo'] = False

        # quando um botão de mouse é precionado
        if event.type == MOUSEBUTTONDOWN:
            blocos.append({'rect':pygame.Rect(event.pos[0], event.pos[1], tamanhoBloco, tamanhoBloco), 'cor':branco, 'vel':1})


    contador += 1
    if contador >= interacoes:
        # adicionando um novo bloco
        contador = 0
        posX = randonTest.randint(0, (largura - tamanhoBloco))
        posY = tamanhoBloco
        velRandom = randonTest.randint(1, vel + 6)
        blocos.append({'rect':pygame.Rect(posX, posY, tamanhoBloco, tamanhoBloco), 'cor':branco, 'vel':velRandom})


    # preenche a cor do fundo
    janela.fill(preto)
    janela.blit(texto, [520, 30]) # coloca o texto na tela

    # movendo o jogador
    moverJogador(jogador, teclas, (largura, altura))

    # desenhando o jogador
    pygame.draw.rect(janela, jogador['cor'], jogador['rect'])

    # checando se jogador bateu em algum bloco ou se bloco saiu da janela para retirá-lo da lista
    for bloco in blocos[:]:
        bateu = jogador['rect'].colliderect(bloco['rect'])
        if bateu or bloco['rect'].y > altura:
            blocos.remove(bloco)
            contClicks += 1
            texto = font.render(str(contClicks), True, verde, preto)


    # movendo e desenhando os blocos
    for bloco in blocos:
        moveBloco(bloco)
        pygame.draw.ellipse(janela, bloco['cor'], bloco['rect'])

    pygame.display.update()
    relogio.tick(40)


