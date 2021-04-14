#!/usr/bin/python3.6
# Problema das sequências alternadas


n = int(input('Informe um valor inteiro: '))
lista = list()

if n > 0:
    a = 1
    while a <= n:

        num = int(input('Informe %dº valor: '%a))
        lista.append(num)

        a += 1

cont = 0

rev = True

while cont < len(lista):
    if (cont % 5 == 0):
        lista.sort(reverse=rev)
    if (rev):
        rev = False
    else:
        rev = True

    print(lista[cont])

    cont += 1

