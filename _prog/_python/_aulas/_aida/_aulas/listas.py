from random import choice
from time import sleep

print('*'*30)
print('\tBem-Vindos a PPT')
print('*'*30)

a = ['pedra', 'papel', 'tesoura']
computador = choice(a)

jogador = 0
escolha = ''
print('''
    [0] ? Pedra
    [1] ? Papel
    [2] ? Tesoura''')
jogador = int(input("Chute a sua palavra: "))

print('JO!')
sleep(1)
print('KEN!')
sleep(1)
print('POW!')
sleep(1)

if jogador == 0:
    escolha = 'pedra'
    if computador == a[0]:
        print("Empate")
    elif computador == a[1]:
        print("Computador vence")
    elif computador == a[2]:
        print("Jogador vence")
elif jogador == 1:
    escolha = 'papel'
    if computador == a[0]:
        print("Jogador vence")
    elif computador == a[1]:
        print("Empate")
    elif computador == a[2]:
        print("Computador vence")
elif jogador == 2:
    escolha = 'tesoura'
    if computador == a[0]:
        print("Computador vence")
    elif computador == a[1]:
        print("Jogador vence")
    elif computador == a[2]:
        print("Empate")

print('Computador jogou "{}" e Jogador jogou "{}".'.format(computador, escolha))        
        
    
