#!usr/bin/python3.6
# Problema do quadrado perfeito

lista = list()

n = int(input('Informe um valor[0 para sair]: '))

while n != 0:
    lista.append(n)
    n = int(input('Informe outro valor[0 para sair]: '))

for i in range(0, len(lista)):
    if (lista[i] * lista[i]) in lista:
        print(lista[i])
        break


