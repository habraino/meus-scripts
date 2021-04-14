from socket import *
import os


HOST = ''# Get host of connection
PORT = 9219# Get port of connection


s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))# Bind the connections
s.listen(4)# Listen 4 clients

print('\033[1;33m[*] Listing...\033[m')

while True:
    c, addr = s.accept()
    print('\033[1;33m[*] Connected by: {} {}\033[m'.format(addr[0], addr[1]))
    
    while True:
        data = input('You: ')
        c.send(bytes(data, 'utf-8'))# send message for client

        data = c.recv(1024)# recive the message of client
        if not data or data == b'exit': break
        print('He: \033[1;33m{}\033[m'.format(data.decode()))

    c.close()
    break
os.system('clear')
s.close()

