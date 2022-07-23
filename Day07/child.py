"""
create a secondary child process to handle
zombie process
"""
from time import sleep
import os


def f1():
    for i in range(3):
        sleep(2)
        print("write code")


def f2():
    for i in range(2):
        sleep(4)
        print("test code")

pid = os.fork()
if pid < 0:
    print("ERROR")
elif pid == 0:
    p = os.fork()
    if pid == 0:
        f2()
    else:
        os.exit()
else:
    os.wait()
    f1()