"""
测试用例
"""
import time
from multiprocessing import Process
from threading import Thread

# 计算
def count(x, y):
    c = 0
    while c < 1000000:
        x += 1
        y += 1
        c += 1


# IO
def io():
    write()
    read()


def write():
    f = open('test', 'w')
    for i in range(1800000):
        f.write("Hello world\n")
    f.close()


def read():
    f = open('test')
    lines = f.readlines()

tm1 = time.time()
for i in range(10):
    count(1,1)
print("single cpu:", time.time()-tm1)


tm2 = time.time()
for i in range(10):
    io()
print("single io:", time.time()-tm2)


jobs =[]
tm3 = time.time()
for i in range(10):
    p = Process(target=count, args = (1,1,))
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()
print("Process cpu:", time.time() - tm3)


jobs =[]
tm4 = time.time()
for i in range(10):
    p = Process(target=io)
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()
print("Process cpu:", time.time() - tm3)

work = []
tm5 = time.time()
for i in range(10):
    t = Thread(target=count, args=(1,1))
    work.append(t)
    t.start()
for i in work:
    t.join()
print("Tread cpu:", time.time()-tm5)


work = []
tm5 = time.time()
for i in range(10):
    t = Thread(target=io)
    work.append(t)
    t.start()
for i in work:
    t.join()
print("Tread io:", time.time()-tm5)