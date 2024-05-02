# Page 139
 
import ctypes
import multiprocessing
import time


def myPi(m, n, PI):
    pi = 0
    for k in range(m, n+1):
        s = 1 if k % 2 else -1
        pi += s / (2 * k - 1)
    with PI:
        PI.value += pi*4


if __name__ == '__main__':
    N = 10000000
    PI = multiprocessing.Value(ctypes.c_double, 0.0)
    p1 = multiprocessing.Process(target=myPi, args=(N//2+1, N, PI))
    t1 = time.perf_counter()
    p1.start()
    myPi(1, N//2, PI)
    p1.join()
    t2 = time.perf_counter()
    print((t2-t1)*1000)
    print(PI.value)
