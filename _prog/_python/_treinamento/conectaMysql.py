import pymysql as mysql


conn = mysql.connect(
	host = "localhost",
	user = "brayen",
	passwd = "hAck12@30",
        database = "teste"
)

cursor = conn.cursor()

cursor.execute('SELECT * FROM lingProg ORDER BY id')
resultado = cursor.fetchall()


print('*'*20)
for i in resultado:
    print('ID: {}\nNome: {}\nAutor: {}'.format(i[0], i[1], i[2]))
    print('*'*20)
