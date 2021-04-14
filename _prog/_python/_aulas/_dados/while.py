from random import randint

computador = randint(1, 10)# sorteia um numero no intervalo de 1 à 10

# declarações das variáveis
jogador = 0
chances = 5
acertou = False
tentativas = 0

print("Nº de Chances: {}".format(chances))

while not acertou and chances != 0:
    jogador = int(input("Chute um número -> "))
    chances -= 1
    tentativas += 1

    if chances < 1:
        print('Você perdeu! O número sorteado é: {}'.format(computador))
        break

    if jogador == computador:
        print('Parabéns! Você acertou com {} tentativas.'.format(tentativas))
        acertou = True
    elif jogador > computador:
        print('Você errou! Chute um número menor!')
        print("Nº de Chances: {}".format(chances))
    elif jogador < computador:
        print('Você errou! Chute um número maior!')
        print("Nº de Chances: {}".format(chances))

print('Fim do Jogo!')


        
