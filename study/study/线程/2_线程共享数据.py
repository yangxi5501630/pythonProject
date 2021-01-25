import threading

'''
多线程和多进程最大的不同在于:
多进程中，同一个变量，各自有一份拷贝存在每个进程中，互不影响
而多线程中，所有变量都由所有线程共享。所以，任何一个变量都可以被任意一个线程修改
因此，线程之间共享数据最大的危险在于多个线程同时修改一个变量，容易把内容改乱了。
'''

num = 0

def run():
    global num
    for i in range(1000000):
        num += 1

if __name__ == "__main__":
    thread1 = threading.Thread(target=run)
    thread2 = threading.Thread(target=run)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print(num)
