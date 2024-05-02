# Page 208
import concurrent.futures
import time


def myPi(m, n):
    pi = 0
    for k in range(m, n+1):
        s = 1 if k % 2 else -1
        pi += s / (2 * k - 1)
    return pi*4


if __name__ == '__main__':
    N = 10000000
    with concurrent.futures.ProcessPoolExecutor(2) as execute:
        t1 = time.perf_counter()
        f1 = execute.submit(myPi, 1, N//2)
        f2 = execute.submit(myPi, N//2+1, N)
        PI = f1.result()
        PI += f2.result()
        t2 = time.perf_counter()
    print((t2-t1)*1000)
    print(PI)
