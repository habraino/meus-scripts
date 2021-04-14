import sqlite3, time

conn = sqlite3.connect('dados.db')
cursor = conn.cursor()

def create() :
    cursor.execute('CREATE TABLE IF NOT EXISTS people (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, '
                   'name TEXT NOT NULL, age INT NOT NULL, date TEXT NOT NULL)')

try:
    create()
except:
    print('error to create a table.')
else:
    print('table was create succesfully.')


def insert(n, i):
    d = time.strftime('%d-%m-%Y  %H:%M:%S')
    cursor.execute('INSERT INTO people VALUES(NULL, ?, ?, ?)', (n, i, d,))
    conn.commit()


def readAll():
    sql = 'SELECT * FROM people'
    print('*'*30)
    for row in cursor.execute(sql,):
        print('ID: {}'.format(row[0]))
        print('Name: {}'.format(row[1]))
        print('Age: {}'.format(row[2]))
        print('Date: {}'.format(row[3]))
        print('*'*30)

def search(arg):
    sql = 'SELECT * FROM people WHERE id = ?'
    print('*' * 30)
    for row in cursor.execute(sql, (arg,)):
        print('ID: {}'.format(row[0]))
        print('Name: {}'.format(row[1]))
        print('Age: {}'.format(row[2]))
        print('Date: {}'.format(row[3]))
        print('*' * 30)

    conn.commit()

def delete(arg):
    sql = 'DELETE FROM people WHERE id = ?'

    cursor.execute(sql, (arg,))
    print('ID %s was deleted succesfully.'%(arg))

insert('Brayen', 21)
insert('John', 25)
insert('Jivaldo', 20)

delete(2)

#readAll()
search(1)
