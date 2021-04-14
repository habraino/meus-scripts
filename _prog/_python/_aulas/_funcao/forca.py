# file_name: forca.py

def jogar():
    print('*********************************************')
    print('\tBem vindo ao Jogo da Forca')
    print('*********************************************')

    secreto = "banana"
    acertou = False
    enforcou = False
    erros = 0
    acertos = ['_','_','_','_','_','_']

    print(acertos)

    while not enforcou and not acertou:
        
        chute = input("Chute uma letra: ")
    
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
