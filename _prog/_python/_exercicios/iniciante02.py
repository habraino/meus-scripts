#!/usr/bin/python3.6
#Problema da média

n = int(input('Entre com quantidades de notas: '))

if n > 0 and n < 1000:
    media = 0
    soma = 0
    a = 1
    valido = 0
    while a <= n:
        nota = float(input(f'Informe {a}ª nota: '))

        if nota >= 0 and nota <= 20:
            soma += nota
            valido += 1
        else:
            pass

        a += 1

    media = soma / valido

    print('Sua média é de: {:.1f}'.format(media))


