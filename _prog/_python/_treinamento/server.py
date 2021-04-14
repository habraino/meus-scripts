import socket

def main():
    host = socket.gethostname()
    port = 12348
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)

    print('[*]\033[1;33m Server is lintening...\033[m')

    while True:
        conn, addr = s.accept()
        print("\033[1;36mGot connection from\033[m %s"%str(addr))

        msg = '[+]\033[1;32mConnection Established\033[m' + '\r\n'
        conn.send(msg.encode('ascii'))
        conn.close()

if __name__ == "__main__":
    main()

