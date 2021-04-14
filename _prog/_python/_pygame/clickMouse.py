import pygame, sys
from pygame.locals import *

def main():
    pygame.init()
    janela = pygame.display.set_mode((500, 400))
    pygame.display.set_caption('Evento click do mouse')

    rel = pygame.time.Clock()
    cor_branca = (255, 255, 255)
    cor_verde = (10, 156, 0)

    # cria um rectângulo
    rect = pygame.Rect(250, 200, 40, 40)


    while True:
        janela.fill(cor_branca)
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()

            '''    
            if evento.type == MOUSEBUTTONDOWN:
                if rect.right != 500:
                    rect = rect.move(10, 0) # move é para teclado
                if rect.right == 500:
                    rect.left = 10

            if evento.type == MOUSEMOTION:
                if rect.left != 10:
                    rect = rect.move(-10, 0)
                if rect.left == 10:
                    rect.left = 10
                    
             '''

            # movendo apartir do teclado
            if evento.type == KEYDOWN:
                if evento.key == K_LEFT:
                    rect.move_ip(-10, 0) # move_ip é usado para teclados
                if evento.key == K_RIGHT:
                    rect.move_ip(10, 0) # move_ip é usado para teclados
                if evento.key == K_UP:
                    rect.move_ip(0, -10) # move_ip é usado para teclados
                if evento.key == K_DOWN:
                    rect.move_ip(-0, 10) # move_ip é usado para teclados

        rect.left, rect.top = pygame.mouse.get_pos()
        # desenha o rectângulo na tela
        pygame.draw.rect(janela, cor_verde, rect)

        pygame.display.update()
        rel.tick(40)

if __name__ == '__main__':
    main()


