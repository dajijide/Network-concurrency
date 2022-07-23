"""
线程锁演示
"""

from threading import Thread, Lock

a = b = 0
lock = Lock()


def value():
    while True:
        lock.acquire()  # 上锁
        if a != b:
            print("a=%d, b=%d" % (a, b))
        lock.release()  # 解锁


t = Thread(target=value)
t.start()
while True:
    with lock:  # 上锁
        a += 1
        b += 1
t.join()
