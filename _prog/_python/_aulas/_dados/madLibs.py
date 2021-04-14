#!python3
#madLibs.py -> Substitui palavras no arquivo txt

import re

fileOpen = open('file.txt', 'r')
ler = fileOpen.read()

comp = re.compile(r'ADJECTIVE|NOUN|VERB')
c = comp.findall(ler)
print(c == None)
if c != None:
    # lê as novas atualizações
    ad = input('Enter an Adjective: ')
    noun = input('Enter an Noun: ')
    verb = input('Enter an Verb: ')

    # faz mudança da palavras no arquivo e escreve atualização no save.txt
    a = ler.replace(c[0], ad).replace(c[1], noun).replace(c[2], verb)
    _save = open('save.txt', 'w')
    _save.write(' %s \n'%(a))

    # fecha os arquivos abertos
    _save.close()
    fileOpen.close()

    # abri o arquivo novamente e escreve seu conteúdo na tela
    ab = open('save.txt')
    print(ab.read())
else:
    print('Words not found in file.')
