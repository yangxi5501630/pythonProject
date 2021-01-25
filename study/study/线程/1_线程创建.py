import threading
from time import sleep

def run(num):
    print(num)
    print("子线程启动: %s" %(threading.current_thread().name))
    sleep(2)
    print("子进程结束: %s" %(threading.current_thread().name))

if __name__ == "__main__":
    print("主线程: %s" %(threading.current_thread().name))

    thread = threading.Thread(target=run, name="runthread", args=(1,))

    thread.start()

    thread.join()
    print("主线程结束.")