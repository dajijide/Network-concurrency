"""
value.py 开辟单一共享内存空间
注意： 共享内存中只能有一个值
"""

from multiprocessing import Process, Value
import time
import random

# 创建共享内存
money = Value('i', 5000)


# 操作共享内存
def man():
    for i in range(30):
        time.sleep(0.2)
        money.value += random.randint(1, 1000)


def girl():
    for i in range(30):
        time.sleep(0.15)
        money.value -= random.randint(100, 800)


p1 = Process(target=man)
p2 = Process(target=girl)
p1.start()
p2.start()
p1.join()
p2.join()

# 获取共享内存
print("一个月余额：", money.value)