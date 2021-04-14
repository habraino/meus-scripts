from random import randint
import os

linhas = ['', '', '', '', '', '', '', '', '']

# meu campo do game desenhado
campo = lambda:print('''
        |       |
   {}\t|   {}\t|   {}
        |       |
-------------------------
        |       |
   {}\t|   {}\t|   {}
        |       |
-------------------------
        |       |
   {}\t|   {}\t|   {}
        |       |
'''.format(linhas[0], linhas[1], linhas[2],
        linhas[3], linhas[4], linhas[5],                 
        linhas[6], linhas[7], linhas[8]))
campo()
# variáveis globais úteis
player = 0
comp = ''
player_X = 'X'
player_O = 'O'
acertou = False
clear = lambda:os.system('clear')

while not acertou:

    put = randint(0, 8)
    player = int(input('Qual sua jogada? [0 - 8]: '))

    # verifica a jogada do computador
    if linhas[put] == '':
        linhas[put] = player_O
    else:
        put = randint(0, 8)
        if linhas[put] == '':
            linhas[put] = player_O
    
    # verifica a jogada do player
    if linhas[player] == '':
        linhas[player] = player_X
    else:
        player = int(input('Qual sua jogada? [0 - 8]: '))
        if linhas[player] == '':
            linhas[player] = player_X
    clear()
    campo()# mostra o campo do game

##############################################################################
#                       VERIFICA SE O PLAYER GANHOU
##############################################################################  
    if linhas[0] == 'X' and linhas[1] == 'X' and linhas[2] == 'X' or linhas[3] =='X'and linhas[4] == 'X' and linhas[5] == 'X' or linhas[6] == 'X' and linhas[7] == 'X' and linhas[8] == 'X' or linhas[0] == 'X' and linhas[4] == 'X' and linhas[8] == 'X' or linhas[2] == 'X' and linhas[4] == 'X' and linhas[6] == 'X' or linhas[0] == 'X' and linhas[3] == 'X' and linhas[6] == 'X' or linhas[1] == 'X' and linhas[4] == 'X' and linhas[7] == 'X' or linhas[2] == 'X' and linhas[5] == 'X' and linhas[8] == 'X':
        print('\033[1;33mYou Win!\033[m')
        acertou = True

##############################################################################
#                       VERIFICA SE O COMPUTADOR GANHOU
##############################################################################  
    if linhas[0] == 'O' and linhas[1] == 'O' and linhas[2] == 'O' or linhas[3] =='O'and linhas[4] == 'O' and linhas[5] == 'O' or linhas[6] == 'O' and linhas[7] == 'O' and linhas[8] == 'O' or linhas[0] == 'O' and linhas[4] == 'O' and linhas[8] == 'O' or linhas[2] == 'O' and linhas[4] == 'O' and linhas[6] == 'O' or linhas[0] == 'O' and linhas[3] == 'O' and linhas[6] == 'O' or linhas[1] == 'O' and linhas[4] == 'O' and linhas[7] == 'O' or linhas[2] == 'O' and linhas[5] == 'O' and linhas[8] == 'O':
        print('\033[1;31mYou Lose!\033[m')
        acertou = True
    
