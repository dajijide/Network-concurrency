"""
Zombie process through signal processing
"""
import os, sys
import signal

# When the child process exits,the parent process ignores the exit behavior,
# and the child process is handled by the system
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

pid = os.fork()
if pid < 0:
    print("ERROR")
elif pid == 0:
    print("Child PID:",os.getpid())
    sys.exit(2)
else:
    while True:
        pass