from multiprocessing import Process
from time import sleep
import os

def run(str):
    while True:
        print("子进程: %s %s %s" %(str, os.getpid(), os.getppid()))
        sleep(1.5)

if __name__ == "__main__":
    print("主进程启动: %s" %(os.getpid()))

    #创建子进程,传递单元素元组
    p = Process(target=run, args=("张三",))

    #启动子进程
    p.start()

    while True:
        print("主进程这里运行")
        sleep(1)
