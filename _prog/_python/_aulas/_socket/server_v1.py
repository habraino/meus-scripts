#-*-encoding: utf-8 -*-

import socket

HOST = ''
PORT = 3433
ADDR = (HOST, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# corresponde a ip, tcp
s.bind(ADDR)# pega ip e porta
s.listen(5)# escuta até 5 clientes


while True:
    print 'wainting for conecctions'
    clientSocket, address = s.accept()
    print 'Connection from', address, 'has bem established'
    while True:
        data = clientSocket.recv(1024)
        if not data: break
        print '\nReceived message:', data
clientSocket.close()

