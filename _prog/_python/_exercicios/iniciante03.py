#!/usr/bin/python3.6
# Problema do número espelho

n = input('Informe um valor em hexadecimal: ')

if n == n[::-1]:
    print('S')
else:
    print('N')


