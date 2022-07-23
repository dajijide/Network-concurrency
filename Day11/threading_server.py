"""
基于threading多线程开发
1.创建套接字
2.循环等待客户端链接
3.创建线程处理客户端请求，主线程继续等待链接
4.客户端退出销毁对应的线程
"""

from socket import *
from threading import Thread
import sys

# 设置全局变量
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send("OK")
    c.close()
    
# 创建套接字
s = socket
s.setsockopt(SOL_SOCKET, SO_REUSEADDR)
s.bind(ADDR)
s.listen(5)

print("listen the port 8888...")

# 循环等待客户端链接
while True:
    try:
        c,addr = s.accept()
        print("connect from",addr)
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        continue

    # 创建线程处理
    t = Thread(target=handle, args=(c,))
    t.setDaemon(True)
    t.start()