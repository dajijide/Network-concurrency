"""
httpserver v2.0
env :3.8
io多路复用 和 http 训练
"""

from socket import *
from select import *


# 具体功能实现
class HTTPServer:
    def __init__(self, host='0.0.0.0', port=8000, dir=None):
        self.host = host
        self.port = port
        self.dir = dir
        self.address = (host, port)
        # 多路复用列表
        self.rlist = []
        self.wlist = []
        self.xlist = []
        # 实例化对象时直接创建套接字
        self.create_socket()
        self.bind()

        # 创建套接字

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        # 绑定地址

    def bind(self):
        self.sockfd.bind(self.address)
        # 启动服务

    def serve_forever(self):
        self.sockfd.listen(3)
        print("listen the port %d" % self.port)
        # IO多路复用接收客户端请求
        self.rlist.append(self.sockfd)
        while True:
            rs, wx, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    print("connect from", addr)
                    self.rlist.append(c)
                else:
                    # 处理请求
                    self.handle(r)

    def handle(self, connfd):
        # 接收HTTTP请求
        request = connfd.recv(4096)
        # 客户端断开
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return
            # 提取请求内容（字节串按行分割）
        request_line = request.splitlines()[0]
        info = request_line.decode().split(' ')[1]
        print(connfd.getpeername(), ':', info)
        # 根据请求内容进行数据整理
        # 分为两类 1.请求网页 2.其他
        if info == '/' or info[-5:] == '.html':
            self.get_html(connfd, info)
        else:
            self.get_data(connfd,info)

    def get_html(self, connfd, info):
        if info == '/':
            # 请求主页
            filename = self.dir + '/index.html'
        else:
            filename = self.dir + info
        try:
            fd = open(filename)
        except Exception:
            # 网页不存在
            response = "HTTP/1.1 404 Not Found\r\n"
            response += 'Content=Type:text/html\r\n'
            response += '\r\n'
            response += '<h1>Sorry...</h1>'
        else:
            # 网页存在
            response = "HTTP/1.1 200 OK\r\n"
            response += 'Content=Type:text/html\r\n'
            response += '\r\n'
            response += fd.read()
        finally:
            # 将响应发送给浏览器
            connfd.send(response.encode())

    # 其他数据
    def get_data(self,connfd,info):
        response = "HTTP/1.1 200 OK\r\n"
        response += 'Content=Type:text/html\r\n'
        response += '\r\n'
        response += "<h1Waiting for httpserver 3.0</h1>"
        connfd.send(response.encode())


# 用户使用HTTPServer
if __name__ == "__main__":
    """
    通过 HTTPServer类快速搭建服务，展示自己的网页
    """
    # 用户决定的参数
    HOST = '0.0.0.0'
    POST = 8000
    DIR = './static'  # 网页存储位置

    httpd = HTTPServer(HOST, POST)  # 实例化对象
    httpd.serve_forever()  # 启动服务
