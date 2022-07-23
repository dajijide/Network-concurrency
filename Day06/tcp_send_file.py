from socket import *

s = socket()
s.bind(('127.0.0.1', 12345))
s.listen(4)

file = open('test.txt', 'rb')
while True:
    data = file.read(1024)
    if not data:
        break
    s.send(data)

file.close()
s.close()