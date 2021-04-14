#!/usr/bin/python3.6
# Problema dos casais

n = int(input('Número de pessoas: '))

contPar = 0
contImpar = 0
cont = 1

while cont <= n:
    numCartao = int(input('Informe o Nº do %dº cartão: '%cont))

    if numCartao % 2 == 0:
        contPar += 1
    else:
        contImpar += 1
    cont += 1

if contPar == contImpar:
    print("S")
else:
    print("N")
