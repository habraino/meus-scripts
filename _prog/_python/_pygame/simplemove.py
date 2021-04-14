import sys, pygame
from pygame.locals import *

pygame.init()

janela = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Simple Move')

# carega a imagem
img = pygame.image.load('bola.png')
img1 = pygame.image.load('bola.png')


# define as cores
fundo = pygame.Color(255, 255, 255)
verde = pygame.Color(0, 255, 0)

# declara as variáveis x e y
x = 0
y = 0


while True:
	for e in pygame.event.get():
		if e.type == QUIT:
			pygame.quit()
			sys.exit()


	janela.fill(fundo)
	janela.blit(img, (x, 50))
	janela.blit(img1, (250, y))


	x += 1
	y += 1

	# move o elemento na tela
	if x > 490:
		x -= 490

	if y > 390:
		y -= 390

	pygame.display.update()
	pygame.display.flip()



