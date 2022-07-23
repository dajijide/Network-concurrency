import os

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    print("Child PID:", os.getpid()) # child pid
    print("Get parent PID", os.getppid()) # parent pid
else:
    print("Get child PID", pid) # child pid
    print("Parent PID:", os.getpid()) # parent pid