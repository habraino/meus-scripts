from conexion import *
import os
from time import sleep

choose = 0# armazena a escolha do usuário

# método que apresenta o menu inicial
def menu():
    print('''\033[1;32m
        [ 1 ] NEW STORE
        [ 2 ] READ STORE
        [ 3 ] UPDATE STORE
        [ 4 ] DELETE STORE
        [ 5 ] SEARCH
        [ 6 ] EXIT
    \033[m''')

while True:# equanto verdadeiro executa
    menu()# chama método menu
    choose = int(input('\033[1;33mWitch your option? \033[m'))# lê escolha do usuário

    if choose == 1:# se escolha for 1
        os.system('clear')# limpa tela
        try:# tenta ler os dados da venda
            n = input('Name of products: ').strip().title()
            p = float(input('Price of products: '))
            q = int(input('Quantity of products: '))
            data_entry(n, p, q)# passa a venda para banco de dados
            os.system('clear')# limpa tela
        except:# caso ocorrer um erro
            print('\033[1;31mError to stores the {}\033[m'.format(n))# mostra essa sms
        else:# senão 
            print('\033[1;33m{} was stored successfully!\033[m'.format(n))# mostra essa sms
    elif choose == 2:# caso escolha for 2
        os.system('clear')#limpa tela
        data_read()# lê os dados do banco de dados
        input('\033[1;32mpress <enter> to continue...\033[m')
        os.system('clear')# limpa tela
    elif choose == 3:# caso escolha for 3
        os.system('clear')# limpa tela
        data_read()# lê os dados do banco de dados
        _id = int(input('Enter with id for update: '))# lê o id
        # aprensenta um menu de opções
        print('''\033[1;32m
            [ 1 ] name   
            [ 2 ] price   
            [ 3 ] quantity \033[m''')
        update = int(input('What you want to update? '))# lê escolha de a ser atualizado
        if update == 1:# caso escolher atualizar nome
            new_name = input('Enter with new name: ')# lê novo nome
            data_update(update, new_name, _id)# atualiza o nome no banco de dados
        elif update == 2:# caso escolher atualizar preço
            new_price = float(input('Enter with new price: '))# lẽ novo preço
            data_update(update, new_price, _id)# atualiza o preço no banco de dados
        elif update == 3:# caso escolher atualizar quantidade
            new_quantity = int(input('Enter with new quantity: '))# lê nova quantidade
            data_update(update, new_quantity, _id)# atualiza a quantidade no banco de dados
    elif choose == 4:# caso escolha for 4
        os.system('clear')# limpa tela
        data_read()# lê os dados do banco de dados
        _id2 = int(input('Enter with id for delete: '))# lê o id do elemento a ser deletado
        # pergunta se quer mesmo deletar dados
        quest = input('Did you want delete that? [y/n]: ').strip().lower()[0]
        if quest != 'n':# se resposta for diferente de não
            data_del(_id2)# deleta o dado no banco de dados
    elif choose == 5:# caso escolha for 5
        os.system('clear')
        print('''\033[1;32m
            [ 1 ] name
            [ 2 ] name and id\033[m''')
        search = int(input('How you want search dates? '))
        if search == 1:# caso usuário desejar buscar por nome
            os.system('clear')# limpa tela
            name = input('Enter with name for to search: ').strip().title()# lê nome
            data_search(name)# procura por nome informado
            input('\033[1;32mpress <enter> to continue...\033[m')
            os.system('clear')# limpa tela
        elif search == 2:# caso usuário desejar buscar por nome e id
            os.system('clear')# limpa tela
            _id3 = int(input('Enter with id for to search: '))# lê id
            name = input('Enter with name for to search: ').strip().title()# lê nome
            data_search(name, _id3)# procura por nome e id informado
            input('\033[1;32mpress <enter> to continue...\033[m')
            os.system('clear')# limpa tela
    elif choose == 6:# caso escolha for 6
        os.system('clear')# limpa tela
        break# quebra a repetição
    else:
        print('\033[1;31mError, choose invalid!!\033[m')

# fim do programa
print('\033[1;36mEXITING...\033[m')
sleep(2)# espera 2 segundos
os.system('clear')# impa tela

