from socket import *

host = '192.168.1.1'
port = 5000

udp = socket(AF_INET, SOCK_DGRAM)
dest = (host, port)
udp.connect(dest)
print('Para sair use Ctrl + X')

msg = input()

while msg != '\x18':
    udp.send(msg)
    msg = input()

udp.close()
