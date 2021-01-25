import threading

#创建一个全局的ThreadLocal对象
#每个线程有独立的存储空间
#每个线程对ThreadLocal对象都可以读写，但是互不影响
#作用：为每个线程绑定一个数据库链接，HTTP请求，用户身份信息等
#这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源
local = threading.local()

def add(a, b):
    a += b
    return a

def run(num):
        local.x = num
        for i in range(5):
            local.x = add(local.x, i)
        print("子进程%s: local.x = %d" %(threading.current_thread().name, local.x))

if __name__ == "__main__":
    thread1 = threading.Thread(target=run, args=(1,))
    thread2 = threading.Thread(target=run, args=(250,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()