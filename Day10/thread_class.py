"""
自定义线程示范
"""
from threading import Thread


# 自定义线程类
class ThreadClass(Thread):
    # 重写父类init
    def __init__(self, *args, **kwargs):
        self.attr = args[0]
        super().__init__()  # 加载父类

    # 假设需要很多步骤完成功能
    def f1(selfself):
        print("step 1")

    def f2(selfself):
        print("step2")

    # 重写run逻辑调用
    def run(self):
        self.f1()
        self.f2()


t = ThreadClass("abc")
t.start()  # 自动运行run
t.join()
