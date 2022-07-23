"""
创建两个进程
分别复制文件的上半部分和下半部分
"""

import os
from multiprocessing import Process

filename = "./face.jpg"
size = os.path.getsize(filename)
# 父进程创建fr 两个子进程使用这个fr会相互影响

# 复制上半部分
def top():
    fr = open(filename, 'rb')
    fw = open("top.jpg", 'wb')
    n = size // 2
    fw.write(fr.read(n))
    fr.close()
    fw.close()

# 复制下半部分
def bot():
    fr = open(filename, 'rb')
    fw = open("bot.jpg", 'wb')
    fr.seek(size // 2, 0)
    fw.write(fr.read())
    fr.close()
    fw.close()

p1 = Process(target=top)
p2 = Process(target=bot)

p1.start()
p2.start()
p1.join()
p2.join()