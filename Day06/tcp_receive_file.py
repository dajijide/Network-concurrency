from socket import *

s = socket()
s.bind(('127.0.0.1', 12345))
s.listen(4)

c, addr = s.accept()
print("connnect form", addr)

file = open('apex.txt', 'wb')

while True:
    data = c.recv(1024)
    if not data:
        break
    file.write()

file.close()
c.close()
s.close()