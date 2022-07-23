"""
基于process的多线程开发
1.创建监听套接字
2.等待接收客户端请求
3.客户端连接创建的进程处理客户端请求
4.原进程继续等待其他客户端连接
5.如果客户端退出，则销毁对应的进程
"""
from socket import *
import os
import signal
from multiprocessing import Process

# 全局变量
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 创建套接字
s = socket
s.setsockopt(SOL_SOCKET, SO_REUSEADDR)
s.bind(ADDR)
s.listen(5)

# 具体处理客户端请求
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send("OK")
    c.close()

# 处理僵尸进程
signal.signal(signal.SIGINT, signal.SIG_IGN)
print("listen the port 8888...")

while True:
    # 循环处理客户端连接
    try:
        c, addr = s.accept()
        print("connect from")
    except KeyboardInterrupt:
        os.exit(0)
    except Exception as e:
        print(e)
        continue
    # 创建子进程处理客户端
    p = Process(target=handle,args=(c,))
    p.daemon = True  # 父进程结束则所有服务终止
    p.start()
    