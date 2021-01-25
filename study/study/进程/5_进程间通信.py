from multiprocessing import  Process, Queue
from time import sleep
import os

def pwrite(q):
    print("子进程: %s开始" %(os.getpid()))
    list = ['A', 'B', 'C', 'D']
    for m in list:
        q.put(m)
        sleep(1)
    print("子进程: %s结束." %(os.getpid()))

def pread(q):
    print("子进程: %s开始" % (os.getpid()))
    while True:
        data = q.get()
        print(data)
    print("子进程: %s结束" %(os.getpid()))

if __name__ == "__main__":
    #创建队列
    q = Queue()

    #创建读进程和写进程
    pw = Process(target=pwrite, args=(q, ))
    pr = Process(target=pread, args=(q, ))

    #启动进程
    pw.start()
    pr.start()

    pw.join()
    pr.terminate()

    print("主进程结束.")








