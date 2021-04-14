from conta import *
from time import sleep
import os

# variávei úteis
numero = ''
saldo = 0.0
limite = 0.0

# método que armazena o menu inicial do programa
def menu():
    print('''\033[1;36m*****************************************\033[m''')
    print('\033[1;31m\t\t Bem-Vindos\033[m')
    print('\033[1;36m*****************************************\033[m')
    print('''\033[1;31m
    \t\t1 → Nova Conta
    \t\t2 → Logar
    \t\t3 → Sair\033[m''')
    print('\033[1;36m*****************************************\033[m')

def menu1():
    print('''\033[1;36m**********************************************\033[m''')
    print('\033[1;31m\t\t Bem-Vindos ao Banco Civil\033[m')
    print('\033[1;36m************************************************\033[m')

while True:
    menu()

    user = int(input('O que desejas fazer? '))

    while user != 3 and (user <= 0 or user > 3):
        user = int(input('O que desejas fazer? '))

    if user == 3:
        os.system('clear')
        break
    
    if user == 1:
        os.system('clear')
        print('\033[1;33mcoletando dados do cliente\033[m')
        nome = input('Nome: ')
        sobrenome = input('SobreNome: ')
        numBi = int(input('Nº de BI: '))
        
        cliente = Cliente(nome, sobrenome, numBi)

        input('\033[1;32m precione <Enter> para continuar...\033[m')
        os.system('clear')
        print('\033[1;33mcoletando dados para nova conta\033[m')
        numero = input('Número: ')
        saldo = float(input('Saldo: '))
        limite = float(input('Limite: '))

        print('Criando nova conta...')
        conta = Conta(numero, cliente, saldo, limite)
        sleep(2)
        os.system('clear')
    
    if user == 2:
        senha = input('entre com seu numero da conta: ')

        if senha == numero:
            menu1()
        else:
            print('Cria nova conta caso ainda não tens uma!')


