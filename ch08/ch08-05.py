# Page 147-148
 
import multiprocessing
import multiprocessing.pool
import time


def myPi(m, n):
    pi = 0
    for k in range(m, n+1):
        s = 1 if k % 2 else -1
        pi += s / (2 * k - 1)
    return pi*4


if __name__ == '__main__':
    N = 10000000
    with multiprocessing.pool.Pool(2) as p:
        t1 = time.perf_counter()
        asr1 = p.apply_async(myPi, args=(1, N//2))
        asr2 = p.apply_async(myPi, args=(N//2+1, N))
        PI = asr1.get()
        PI += asr2.get()
        t2 = time.perf_counter()
    print((t2-t1)*1000)
    print(PI)
