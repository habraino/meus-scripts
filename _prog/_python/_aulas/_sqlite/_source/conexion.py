import sqlite3 as db
from time import strftime

# pega o caminho completo e cria um nov db
path = '/home/brayen/Documentos/_project/_python/_aulas/_sqlite/_database'
wayAll = '{}/vendas.db'.format(path)
conn = db.connect(wayAll)# conecta o banco de dados
cursor = conn.cursor()# começa o cursor

# método para criar uma nova tabela
def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS store(id INTEGER PRIMARY KEY AUTOINCREMENT ,\
                        name TEXT NOT NULL,\
                        price REAL NOT NULL,\
                        quantity INT NOT NULL,\
                        total REAL NOT NULL,\
                        date TEXT NOT NULL)')
try:# tenta criar uma nova tabela
    create_table()         
except:# caso ocorra um erro
    print('ERROR TO CREAT A TABLE')# mostra essa sms
else:# senão 
    print('TABLE WAS CREATED SUCCESSFULLY!')# mostra essa sms
       
# método para inserir dados na tabela
def data_entry(n, p, q):
    date = strftime("%d-%m-%Y %H:%M:%S")
    tot = p * q # calculo total do preço
    cursor.execute('INSERT INTO store VALUES (NULL, ?, ?, ?, ?, ?)', (n, p, q, tot, date,))
    conn.commit()

# método para ler dados da table
def data_read():
    sql = 'SELECT * FROM store'
    for row in cursor.execute(sql, ):
        print('*'*45)
        print('ID..................: {}'.format(row[0]))
        print('Name................: {}'.format(row[1]))
        print('Price...............: {} Ndbs'.format(row[2]))
        print('Quantity............: {}'.format(row[3]))
        print('Price Total.........: {} Ndbs'.format(row[4]))
        print('Date of Store.......: {}'.format(row[5]))
        print('*'*45)

# método para atualizar dados na tabela
def data_update(arg, arg1, arg2):
    if arg == 1:
        cursor.execute('UPDATE store set name = ? WHERE id = ?', (arg1, arg2))
        conn.commit()
    elif arg == 2:
        cursor.execute('UPDATE store set price = ? WHERE id = ?', (arg1, arg2))
        conn.commit()
    elif arg == 3:
        cursor.execute('UPDATE store set quantity = ? WHERE id = ?', (arg1, arg2))
        conn.commit()

# método para deletar dados na tabela
def data_del(arg):
    sql = 'DELETE from store WHERE id = ?'
    cursor.execute(sql, (arg,))
    print('\033[1;33mID {} was deleted successfully!\033[m'.format(arg))
    conn.commit()


# método para pesquisar dados na tabela
def data_search(arg, args=None):
    sql = 'SELECT * FROM store WHERE name = ? and id = ?'# pesquisa pelo nome e id
    sql2 = 'SELECT * FROM store WHERE name = ?'# pesquisa pelo nome apenas
    if args is not None:
        for i in cursor.execute(sql, (arg, args,)):
            print('*'*45)
            print('ID..................: {}'.format(i[0]))
            print('Name................: {}'.format(i[1]))
            print('Price...............: {} Ndbs'.format(i[2]))
            print('Quantity............: {}'.format(i[3]))
            print('Price Total.........: {} Ndbs'.format(i[4]))
            print('Date of Store.......: {}'.format(i[5]))
            print('*'*45)
    else:
        for b in cursor.execute(sql2, (arg,)):
            print('*'*45)
            print('ID..................: {}'.format(b[0]))
            print('Name................: {}'.format(b[1]))
            print('Price...............: {} Ndbs'.format(b[2]))
            print('Quantity............: {}'.format(b[3]))
            print('Price Total.........: {} Ndbs'.format(b[4]))
            print('Date of Store.......: {}'.format(b[5]))
            print('*'*45)
    conn.commit()

