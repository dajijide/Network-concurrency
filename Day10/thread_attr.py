"""
thread_attr.py
线程属性演示
"""

from threading import Thread
from time import sleep


def fun():
    sleep(3)
    print("线程属性测试")


t = Thread(target=fun)
t.setDaemon(True)
t.start()
t.setName("Tedu")
print("name:", t.getName())
print("is alive:", t.is_alive())
print("is daemon:", t.isDaemon())
