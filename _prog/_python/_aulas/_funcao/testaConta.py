from conta import *
from time import sleep
import os

# variávei úteis
numero = ''
saldo = 0.0
limite = 0.0
user = 0
user1 = 0
conta = {}

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

# método que armazena o menu das opções da conta
def menu1():
    print('\033[1;36m**********************************************************\033[m')
    print('\033[1;31m\t\t Bem-Vindos ao Banco Civil\033[m')
    print('\033[1;36m**********************************************************\033[m')
    print('''\033[1;31m
    \t\t\t1 → Depositar
    \t\t\t2 → Sacar
    \t\t\t3 → Transferir
    \t\t\t4 → Extrato
    \t\t\t5 → Voltar\033[m''')
    print('\033[1;36m**********************************************************\033[m')


while user != 3:
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
    
    # se usuário escolher logar
    if user == 2:
        senha = input('entre com seu numero da conta: ')
        if senha == numero:
            while True:
                os.system('clear')
                menu1()
                user1 = int(input('O que desejas fazer? '))

                # se usuário desejar depositar dinheiro
                if user1 == 1:
                    valor = float(input('Quanto desejas depositar? '))
                    conta.depositar(valor)
                    print('\033[1;33mO {} {} acabou de depositar {}Ndbs.'.format(conta.cliente.nome, conta.cliente.sobrenome, valor))
                    sleep(2)
                
                # se usuário desejar fazer um saque no banco
                elif user1 == 2:
                    valor = float(input('Quanto desejas depositar? '))
                    conta.sacar(valor)
                    print('\033[1;33mO {} {} acabou de sacar {}Ndbs.'.format(conta.cliente.nome, conta.cliente.sobrenome, valor))
                    sleep(2)
                
                # se usuário desejar efetuar uma transferência para outra conta
                elif user1 == 3:
                    valor = float(input('Quanto desejas transferir? '))
                    destino = input('Insira o número do receptor: ')

                    if destino in conta.numero:
                        conta.transferir(destino, valor)
                        print('\033[1;33mO {} {} acabou de sacar {}Ndbs.'.format(conta.cliente.nome, conta.cliente.sobrenome, valor))
                    else:
                        print('\033[1;31mNão foi possível efetuar a transferência!\033[m')
                
                # se usuário desejar ver seu saldo total
                elif user1 == 4:
                    conta.extrato()
                    input('\033[1;32m precione <Enter> para continuar...\033[m')

                # volta para o menu inicial
                if user1 == 5:
                    os.system('clear')
                    break
        else:
            print('Cria nova conta caso ainda não tens uma!')


