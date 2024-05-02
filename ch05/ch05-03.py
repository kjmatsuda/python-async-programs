# Page 90 (Bottom)
from cmath import sqrt
import threading
import time

myCounter = 0
countlock = threading.Lock()


def count():
    global myCounter
    countlock.acquire()
    for i in range(100000):
        temp = myCounter+1
        x = sqrt(2)
        myCounter = temp
    countlock.release()


thread1 = threading.Thread(target=count)
thread2 = threading.Thread(target=count)
t1 = time.perf_counter()

thread1.start()
thread2.start()
thread1.join()
thread2.join()

t2 = time.perf_counter()
print((t2-t1)*1000)
print(myCounter)
