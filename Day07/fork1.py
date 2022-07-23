import os
from time import sleep
print("----------------------")
b = 3
pid = os.fork()
if pid < 0:
    print("Create process failed")
elif pid == 0:
    print("the new process")
    print("b:", b)
    b = 1000
else:
    sleep(1)
    print("the old process")
    print("b", b)
print("b::", b)
