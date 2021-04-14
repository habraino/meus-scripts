#!/usr/bin/python3.6
# Problema da competição alien

n = int(input('Informe um valor: '))
texto = str(input('Insira o texto: ')).lower().replace('.', ' ')

cont = 0

s = texto.split()
for i in s:
    if i.isalpha():
        if len(i) == n:
            cont += 1
print(cont)

