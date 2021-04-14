from random import randint

computador = randint(1, 10)# sorteia um numero no intervalo de 1 à 10

# declarações das variáveis
jogador = 0
chances = 5
acertou = False
tentativas = 0

print('********************************************************************')
print('''
    Olá, eu sou seu computador e pensei em um número entre 1 à 10...
    Vamos ver se você consegue advinhar...
''')
print('********************************************************************')
print("Nº de Chances: {}".format(chances))

while not acertou:
    jogador = int(input("Chute um número -> "))
    chances -= 1
    tentativas += 1

    if chances == 0 and jogador != computador:
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


        
