import threading, time

#事件对象
event = threading.Event()

def run():
    for i in range(5):
        # 等待事件出发
        print("子进程 start: %d" % (i))
        event.wait()
        # 重置
        event.clear()
        print("子进程 end: %d" % (i))

t = threading.Thread(target=run)
t.start()

print("主线程开始.")
for i in range(5):
    time.sleep(2)
    #触发事件
    event.set()

t.join()

print("主线程结束.")