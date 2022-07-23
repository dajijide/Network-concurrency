"""
gevent server 基于协程的tcp并发
思路：1.将每个客户端的处理设置为协程函数
     2.让socket模块下的阻塞可以触发协程跳转
"""
import gevent
from gevent import monkey
monkey.path_all()   # 执行脚本，修改socket阻塞
import socket

# 创建套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sockfd.bind(('127.0.0.1', 8888))
sockfd.listen(7)

def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print(data)
        n = c.send(b'OK')

# 循环接收客户端链接
while True:
    c, addr = sockfd.accept()
    print("Connect from", addr)
    # handle(c) # 处理具体的客户端请求
    gevent.spawn(handle,c)  # 协程方案
