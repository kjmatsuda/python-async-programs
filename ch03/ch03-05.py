# Page 64
import time
import multiprocessing


def myPi(m, n):
    pi = 0
    s = -1
    for k in range(m, n):
        s = -1*s
        pi += s / (2 * k - 1)
    print(4*pi)


if __name__ == '__main__':
    import multiprocessing
    import multiprocessing.connection
    import time
    N = 1000000
    p1 = multiprocessing.Process(target=myPi, args=(N//2+1, N))
    t1 = time.perf_counter()
    p1.start()
    myPi(1, N//2)
    p1.join()
    t2 = time.perf_counter()
    print((t2-t1)*1000)
