from socket import *

host = ''
port = 5000

udp = socket(AF_INET, SOCK_DGRAM)
orig = (host, port)

udp.bind(orig)

while True:
    msg, cliente = udp.recvfrom(1024)
    print(msg, cliente)

udp.close()
