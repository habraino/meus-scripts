#!/usr/bin/python3.6
# Problema da soma reservada 

# retorna inverso do num
def rev(x):
    a = str(x)
    x = int(a[::-1])

    return x

# retorna soma dos inversos
def soma(n, m):
    return rev(rev(n) + rev(m))

n = int(input('Informe 1º valor: '))
m = int(input('Informe 2º valor: '))

print('A soma do inverso é: {}'.format(soma(n, m)))

