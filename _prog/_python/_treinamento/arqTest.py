import random

palavra = list()
with open('teste.txt') as file:
    [palavra.append(f.strip()) for f in file]

sorteio = random.choice(palavra)
acerto = ['_' for _ in sorteio]

print(acerto)

acertou = False

while not acertou:
    letra = str(input('Insira uma letra: ')).strip().upper()
    if letra in sorteio:
        pos = 0
        for s in sorteio:
            if letra == s:
                acerto[pos] = letra
                print(acerto)
            pos += 1

    if '_' not in acerto:
        acertou = True
        print('Você acertou!')
        print('A palavra sorteada é: {}'.format(sorteio))


