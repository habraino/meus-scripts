import socket 

host = socket.gethostname()
port = 12348

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port))
    s.settimeout(3)
    data, addr = s.recvfrom(1024)
    print('recevied from', addr)
    print('obtained:', data.decode('ascii'))
    s.close()
except socket.timeout:
    print('No connection between client and server')    
    s.close()


