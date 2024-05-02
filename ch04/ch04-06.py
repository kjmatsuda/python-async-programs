# Page 78
 

import threading
import time


def myPi(m, n):
    pi = 0
    for k in range(m, n+1):
        s = 1 if k % 2 else -1
        pi += s / (2 * k - 1)
    print(4*pi)


N = 10000000
thread1 = threading.Thread(target=myPi, args=(N//2+1, N))
t1 = time.perf_counter()
thread1.start()
myPi(1, N//2)
thread1.join()
t2 = time.perf_counter()
print((t2-t1)*1000)
 
