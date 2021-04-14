import sqlite3 as db 

path = '/home/brayen/Documentos/_python/_aulas/_sqlite/_database'
wayAll = '{}/primeiro.db'.format(path)
conn = db.connect(wayAll)
cursor = conn.cursor()

# create a new table
def crate_table():
    try:
        cursor.execute('CREATE TABLE IF NOT EXISTS data(name TEXT, age INT)')
    except:
        print('Error to create the Table')
    else:
        print('Table was created successfully!')
crate_table()

# insertthe dates in table
def data_entry():
    try:
        cursor.execute('INSERT INTO data VALUES(?, ?)', ("Brayen", 20))
        cursor.execute('INSERT INTO data VALUES(?, ?)', ("Brayen", 19))
        conn.commit()
    except:
        print('Error to insert dates!')
    else:
        print('Dates inserted successfully!')
data_entry()   

sql = 'SELECT * FROM data WHERE name = ? and age = ?'
sql2 = 'SELECT * FROM data WHERE name = ?'

# read dates
def read_data(arg, args=None):
    if args is not None:
        if 'Brayen' in arg:
            for row in cursor.execute(sql, (arg, args,)):
                print(row)
        else:
            print('Error name not found!')
    else:
        if 'Brayen' in arg:
            for row in cursor.execute(sql2, (arg,)):
                print(row)
        else:
            print('Error name not found!')

read_data('John')
