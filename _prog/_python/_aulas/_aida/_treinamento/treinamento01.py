'''
Escreva um programa em Python que pede ao utilizador que lhe forneça um número
e que escreve positivo, negativo ou zero, caso o número seja, respectivamente, maior,
menor ou igual a zero.
'''

numero = int(input('Informe um número: '))

if numero > 0:
    print('Positivo')
elif numero < 0:
    print('Negativo')
else:
    print('Zero')

