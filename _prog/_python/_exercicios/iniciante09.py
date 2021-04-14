#!/usr/bin/python3.6
# Problema dos sucessores

sucessor = list()

i = int(input('Informe um valor [0 para sair]: '))

while i != 0:
    sucessor.append(i + 1)
    i = int(input('Informe outro valor [0 para sair]: '))

print("Os sucessores são:", end=' ')
for i in sucessor:
    print(i, end=' ')
