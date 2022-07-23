from tcp_server import *

sockfd = socket()
server_addr = ('127.0.0.1', 8888)
sockfd.connect(server_addr)

while True:
    date = input("Msg>>")
    if not date:
        break
    sockfd.send(date.encode())
    date = sockfd.recv(1024)
    print("Sever:", date.decode())

sockfd.close()
