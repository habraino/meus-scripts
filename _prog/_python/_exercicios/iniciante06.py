#!/usr/bin/python3.6
# Problema do quadrado gêmeo das partes

num = int(input('Informe um valor inteiro: '))

trans = str(num)

tam = int(len(trans) / 2)
pri = 0

if num % 100 == 0:
    pri = int(trans[:tam+1])
else:
    pri = int(trans[:tam])

seg = int(trans[tam:])
soma = pri + seg

if (soma * soma) == num:
    print(1)
else:
    print(0)
