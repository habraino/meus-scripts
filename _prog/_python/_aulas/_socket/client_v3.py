# file_name: client_v3.py

from socket import *
import os

HOST = ''
PORT = 9219

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    msg = s.recv(1024)
    if not msg: break
    print('He: \033[1;33m{}\033[m'.format(msg.decode()))

    data = input('You: ')
    s.send(bytes(data, 'utf-8'))

    if data == 'exit':
        break
os.system('clear')
s.close()
   