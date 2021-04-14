'''
Escreva um programa em Python que pede ao utilizador que lhe forneça um número
correspondente ao raio de um círculo e que escreve a área do círculo. A área de um círculo
de raio r é dada pela fórmula πr² . Use o valor 3.14 para a constante π.
'''

print('*'*50)
print('\t\tA área do Círculo')
print('*'*50)

raio = int(input('Raio -> '))

pi = 3.14

area = pi * (raio * raio)

print('A área do cícrculo é de: {}'.format(area))


