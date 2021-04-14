#!usr/bin/python3.6
#__author__= Habraino de Deus
# file_name = CRUDINPY

import pymysql as mysql
import os
from time import sleep 

class ConnectionDAO:

    """
    ===================================================================
                            Documentação do Programa
    ===================================================================
    ConnectionDAO: class
    --------------
    Uma classe para auxiliar o uso do banco de dados MySql.

    Métodos:
    --------

    Create: create
        Cria uma nova tabela no meu banco de dados
    
    Insert: insert
        Insere um novo elemento na tabela

        Name: name  
            Nome da linguagem em especial
        Author: author
            Nome do criador da linguagem
    
    Read: read
        Faz leitura de todos elementos da tabela
    
    Search: search
        Faz pesquisa de um elemento da tabela

        Arg: arg
            Item a ser pesquisado
    
    SearchBY: searchBy
        Efetua pesquisa de um grupo de coluna da tabela

        Arg: arg
            Coluna a ser pesquisado
    
    Delete: delete
        Deleta uma linha específica da tabela

        Item: item=int
            O item a ser deletado
        
        Returns:
        --------
        Retorna True caso o item exista
        Retorna False caso o item não exista
    ===================================================================
    """
    
    # faz a conexão com o db
    __conn = mysql.connect(
        host="localhost",
        user="root",
        passwd="hAck12@2020",
        database="teste"
    )
    # criar um cursor
    cursor = __conn.cursor()

    # método para criar nova tabela
    def create(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS lingProg (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,\
            name VARCHAR(100) NOT NULL, author VARCHAR(100) NOT NULL)
        ''')

    # método para inserir dados
    def insert(self, name, author):
        self.cursor.execute("INSERT INTO lingProg (name, author) VALUES ('%s', '%s')"%(name, author))
        self.__conn.commit()

    # método para ler todos dados do db
    def read(self):
        self.cursor.execute('SELECT * FROM lingProg ORDER BY id')
        rows = self.cursor.fetchall()
        print('*'*40)
        for row in rows:
            print(f'ID.......: {row[0]}')
            print(f'Nome.....: {row[1]}')
            print(f'Autor....: {row[2]}')
            print('*'*40)
    
    # método para pesquisar por um elemento pelo seu nome
    def search(self, arg):
        self.cursor.execute('SELECT * FROM lingProg')
        lista = self.cursor.fetchall()
        
        for i in lista:
            if arg in i[1]:
                self.cursor.execute('SELECT * FROM lingProg WHERE name like "%s"'%(arg))

                rows = self.cursor.fetchall()
                print('*'*40)
                for row in rows:
                    print(f'ID.......: {row[0]}')
                    print(f'Nome.....: {row[1]}')
                    print(f'Autor....: {row[2]}')
                    print('*'*40)

    # método para pesquisar por uma coluna específica
    def searchBy(self, column):
        self.cursor.execute('SELECT %s FROM lingProg'%(column))
        itens = self.cursor.fetchall()
        cont = 1
        print('*'*30)
        print('\tLista dos(as) %s'%(column))
        print('*'*30)
        for item in itens:
            print('{}º........: {}'.format(cont, item))
            cont += 1
        print('*'*30)

    # método para deletar um elemento no DB
    def delete(self, item=int):
        self.cursor.execute('SELECT id FROM lingProg WHERE id LIKE "%d"'%(item))
        lista = self.cursor.fetchall()
        if len(lista) > 0:
            self.cursor.execute('DELETE FROM lingProg WHERE id LIKE "%d";'%(item))
            self.__conn.commit()
            return True
        else:
            return False


# ==== começa a execução do programa ====
# crio nova instância da classe ConnectionDAO
connection = ConnectionDAO()
    

# verifica os possiveis erros
try:
    connection.create()
except:
    print("ERROR TO CREATE A NEW TABLE.")
else:
    print("NEW TABLE WAS CREATED SUCCESSFYLLY.")


# ==== começa a execução do programa ====
# crio nova instância da classe ConnectionDAO
connection = ConnectionDAO()

# algumas variáveis globais
sair = False
limpar = lambda:os.system('clear') # função para limpar tela
precione_enter = lambda:input('Precione <enter> para continuar...')

# enquanto for verdadeiro continua
while not sair:
    # menu das opções
    print('''
        BEM VINDO AO CRUD USANDO MYSQL DB

        Seleciona as opções que se seguem:

        1 → Inserir
        2 → Ler
        3 → Pesquisar
        4 → Pesquisar por
        5 → Atualizar
        6 → Apagar
        7 → Sair/Fechar
    ''')

    # pede para usuário informar sua opção
    user = int(input("O que desejas fazer? "))
    limpar()

    # caso usuário deseja sair
    if user == 7: 
        sair = True
        print('Saindo...')
        sleep(2)
        limpar()

    # caso usuário deseje inserir dados na tabela
    if user == 1:
        n = input('Insere o nome da linguagem: ')
        a = input('Insere o nome do autor da linguagem: ')
        while n == '' or a == '':
            n = input('Por favor..Insere o nome da linguagem: ')
            a = input('Por favor..Insere o nome do autor da linguagem: ')
        connection.insert(n, a) 
        print('Item inserido com sucesso!')
        precione_enter()
        limpar()

    # caso usuário deseje ler todos dados
    elif user == 2:
        connection.read()
        precione_enter()
        limpar()
    # pesquisar por um elemento pelo seu nome
    elif user == 3:
        p = input('Informe o nome da linguagem a ser pesquisada: ').title()
        connection.search(p)
        precione_enter()
        limpar()
    # deletar o item pelo seu id
    elif user == 6:
        d = int(input("Insere o id item a ser deletado: "))
        per = input('Desejas deletar o item selecionado? [s/n]: ').strip().lower()[0]
        if per == 's' and connection.delete(d) == True:
            print('Item deletado com sucesso!')
            precione_enter()
            limpar()
        elif per == 's' and connection.delete(d) == False:
            print('Item não encontrado!') 
        else:
            print('A acção foi cancelada!')

