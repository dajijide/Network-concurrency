import socket

sockfd = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
sockfd.bind(('127.0.0.1', 8888))

sockfd.listen(7)

while True:
    print("waiting for connect...")
    try:
        connfd, addr = sockfd.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        print("")
        break
    except Exception as e:
        print()
        continue

    while True:
        date = connfd.recv(1024)
        if not date:
            break
        print("ecvice", date)
        n = connfd.send(b'hello')
        print("dasongl%dgezijie" % n)

    connfd.close()
sockfd.close()