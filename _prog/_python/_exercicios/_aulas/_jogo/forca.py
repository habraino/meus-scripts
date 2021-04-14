# file_name: forca.py

import random

def jogar():
    print('*********************************************')
    print('\tBem vindo ao Jogo da Forca')
    print('*********************************************')

    arq = open('arquivo.txt', 'r')# carrega o arquivo com palavras secretas
    palavras = []# cria uma lista vazia

    # faz leitura das palavras secretas e adiciona na lista
    for linha in arq:
        linha = linha.strip()
        palavras.append(linha)
    arq.close()# fecha o arquivo txt

    sorteio = random.choice(palavras)# escolhe apenas uma palavra na lista


    secreto = sorteio.lower()
    acertou = False
    enforcou = False
    erros = 0
    acertos = ['_' for letra in secreto]

    print(acertos)

    while not enforcou and not acertou:
        
        chute = input("Chute uma letra: ").strip().lower()
    
        if chute in secreto: 
            pos = 0
            for i in secreto:
                if chute.lower() == i.lower():
                    acertos[pos] = i
                pos += 1
        else:
            erros += 1
        
        enforcou = erros == 6
        acertou = '_' not in acertos
        print(acertos)
    
    if acertou:
        print('Você ganhou!')
    else:
        print('Você perdeu!')
    
    print("Fim do Jogo!")

jogar()
