# Page 149 (bottom)
 
import multiprocessing
import multiprocessing.pool
import time


def myPi(r):
    m, n = r
    pi = 0
    for k in range(m, n+1):
        s = 1 if k % 2 else -1
        pi += s / (2 * k - 1)
    return pi*4


if __name__ == '__main__':
    N = 10000000
    with multiprocessing.pool.Pool(2) as p:
        t1 = time.perf_counter()
        asr = p.map_async(myPi, [(1, N//2), (N//2+1, N)])
        res = asr.get()
        t2 = time.perf_counter()

    print((t2-t1)*1000)
    PI = res[0]+res[1]
    print(PI)
