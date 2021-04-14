from socket import *

HOST = ''
PORT = 2224

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)

conn, adrres = s.accept()
data = conn.recv(1024)
print data
conn.send('Message of server!')

s.close()

