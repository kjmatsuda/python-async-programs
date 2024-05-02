# Page 203-204
import concurrent.futures
import threading
import time
from cmath import sqrt

myCounter = 0
countlock = threading.Lock()


def count():
    global myCounter
    for i in range(100000):
        with countlock:
            temp = myCounter+1
            x = sqrt(2)
            myCounter = temp


with concurrent.futures.ThreadPoolExecutor() as execute:
    t1 = time.perf_counter()
    f1 = execute.submit(count)
    f2 = execute.submit(count)
    concurrent.futures.wait(
        [f1, f2], return_when=concurrent.futures.ALL_COMPLETED)
    t2 = time.perf_counter()
print((t2-t1)*1000)
print(myCounter)
