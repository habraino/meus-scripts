from time import strftime
import sqlite3

conn = sqlite3.connect('teste.db')
cursor = conn.cursor()

def criar():
    cursor.execute('CREATE TABLE IF NOT EXISTS pessoa(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, idade INT NOT NULL, data TEXT NOT NULL)')

try:
    criar()
except:
    print('Erro ao criar banco de dados')
else:
    print('Banco de dados foi criado com sucesso!')

def inserir(n, i):
    data = strftime('%d-%m-%Y %H:%M:%S')
    cursor.execute('INSERT INTO pessoa VALUES(NULL, ?, ?, ?)', (n, i, data,))
    conn.commit()

def pesquisar(p):
    sql = 'SELECT * FROM pessoa WHERE nome = ?'
    for row in cursor.execute(sql, (p,)):
        line = '*'*45
        print(line)
        print('Id....................: {}'.format(row[0]))
        print('Nome..................: {}'.format(row[1]))
        print('Idade.................: {}'.format(row[2]))
        print('Data..................: {}'.format(row[3]))
        print(line)

def read():
    sql = 'SELECT * FROM pessoa'
    c = cursor.execute(sql, )
    for row in c.fetchall():
        line = '*'*45
        print(line)
        print('Id....................: {}'.format(row[0]))
        print('Nome..................: {}'.format(row[1]))
        print('Idade.................: {}'.format(row[2]))
        print('Data..................: {}'.format(row[3]))
        print(line)

user = int(input('1 -> Insert\n2 -> Read\n3 -> Search\nWhat you wanna do? '))
if user == 1:
    try:
        n = str(input('Type your name: ')).strip()
        i = int(input('Type your age: '))
        inserir(n, i)
    except:
        print('Error to insertting person.')
    else:
        print(f'{n} was inserted successfully!')
elif user == 2: 
    read()
elif user == 3:
    p = input('Type name of people to search: ').strip().title()
    pesquisar(p)


