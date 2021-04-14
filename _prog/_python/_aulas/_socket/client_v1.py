#-*-encoding: utf-8 -*-

import socket

HOST = 'localhost'
PORT = 3433
ADDR = (HOST, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# corresponde a ip, tcp
s.connect(ADDR)# pega ip e porta
data = ''
while True:
    while data != 'sair':
        data = raw_input('> ') 
        s.send(data)
    data = s.recv(1024)
    if not data: break  
    print 'coneccted by:', ADDR
s.close()
