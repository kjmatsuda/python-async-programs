# Page 92-93
import threading
import time

countlock1 = threading.Lock()
countlock2 = threading.Lock()
myCounter1 = 0
myCounter2 = 0


def count1():
    global myCounter1
    global myCounter2
    for i in range(100000):
        countlock1.acquire()
        myCounter1 += 1
        countlock2.acquire()
        myCounter2 += 1
        countlock2.release()
        countlock1.release()


def count2():
    global myCounter1
    global myCounter2
    for i in range(100000):
        countlock2.acquire()
        myCounter2 += 1
        countlock1.acquire()
        myCounter1 += 1
        countlock1.release()
        countlock2.release()


thread1 = threading.Thread(target=count1)
thread2 = threading.Thread(target=count2)
t1 = time.perf_counter()

thread1.start()
thread2.start()
thread1.join()
thread2.join()

t2 = time.perf_counter()
print((t2-t1)*1000)
print(myCounter1)
