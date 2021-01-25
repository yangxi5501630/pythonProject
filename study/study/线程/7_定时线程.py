import threading

def run():
    print("hello,thread")

t = threading.Timer(5, run)
t.start()
t.join()
