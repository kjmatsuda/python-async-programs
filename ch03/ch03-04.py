# Page 57
import time
import multiprocessing


def myPi(m, n):
    pi = 0
    for k in range(m, n+1):
        s = 1 if k % 2 else -1
        pi += s / (2 * k - 1)
    print(4*pi)


if __name__ == '__main__':
    N = 10000000
    p1 = multiprocessing.Process(target=myPi, args=(N//4+1, N//4*2))
    p2 = multiprocessing.Process(target=myPi, args=(N//4*2+1, N//4*3))
    p3 = multiprocessing.Process(target=myPi, args=(N//4*3+1, N))

    t1 = time.perf_counter()
    p1.start()
    p2.start()
    p3.start()
    myPi(1, N//4)
    p1.join()
    p2.join()
    p3.join()
    t2 = time.perf_counter()
    print((t2-t1)*1000)
