import threading
import time

bar  = threading.Barrier(2)

def run():
    print("%s....start." %(threading.current_thread().name))
    time.sleep(1)
    bar.wait()  
    print("%s: end." %(threading.current_thread().name))

if __name__ == "__main__":
    for i in range(8):
        threading.Thread(target=run).start()