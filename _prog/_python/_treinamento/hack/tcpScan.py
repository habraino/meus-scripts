import os
import platform
import socket
from datetime import datetime

net = input('Enter the Network Address: ')
net1 = net.split('.')

a = '.'

net2 = net1[0]+a+net1[1]+a+net1[2]+a

st1 = int(input('Enter the Start Number: '))
en1 = int(input('Enter the Last Number: '))
en1 += 1

t1 = datetime.now()

def scan(addr):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((addr, 135))

    if result == 0:
        return 0
    else:
        return 1

def run():
    for ip in range(st1, en1):
        addr = net2+str(ip)

        if scan(addr):
            print(addr, "is live.")

if __name__ == "__main__":
    run()
    t2 = datetime.now()
    total = t2 - t1
    print("Scanning completed in:", total)

    