"""
chat room
env:python3.9
socket,udp & fork
"""
from socket import *
import os, sys

"""
全局变量: Many packing modules need to be used 
or have a certain fixed meaning
"""

# 服务端地址
ADDR = ("0.0.0.0", 8889)

# 存储用户{name ; address}
user = {}


# 登录
def do_login(s, name, addr):
    if name in user or "管理员" in name:
        s.sendto("该用户存在".encode(), addr)
        return
    s.sendto(b'OK',addr)  # 可以进入聊天室

    # 通知其他人
    msg = "\n欢迎'%s'进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(), user[i])
    user[name] = addr


# 退出聊天室
def do_quit(s, name):
    msg = "\n%s 退出聊天室" % name
    for i in user:
        if i != name:  # 其他人
            s.sendto(msg.encode(), user[i])
        else:
            s.sendto(b'Exit', user[i])
    del user[name]   # 删除用户


# 聊天
def do_chat(s, name, text):
    msg = "\n%s: %s" % (name, text)
    for i in user:
        # 刨除其本人
        if i != name:
            s.sendto(msg.encode(), user[i])


# 处理请求
def do_request(s):
    while True:
        data, addr = s.recvfrom(1024)
        tmp = data.decode().split(' ')  # 拆分请求
        # 根据不同的请求类型具体执行不同的事情
        # L 进入  C 聊天  Q 退出
        if tmp[0] == 'L':
            do_login(s, tmp[1], addr)   # 执行具体工作
        elif tmp[0] == 'C':
            # 以空格拼接列表内容
            text = ' '.join(tmp[2:])
            do_chat(s, tmp[1], text)
        elif tmp[0] == 'Q':
            do_quit(s, tmp[1])


# 建立网络
def main():
    # udp服务
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)

    pid = os.fork()
    if pid == 0:  # 子进程处理管理员消息
        while True:
            msg = input("管理员消息：")
            msg = "C 管理员 " + msg
            s.sendto(msg.encode(), ADDR)
    else:
        # 请求处理函数
        do_request(s)


main()
