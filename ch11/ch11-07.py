# Page 205
import concurrent.futures
import multiprocessing
import time
import ctypes


def counter():
    global count
    for i in range(10000):
        with count:
            temp = count.value+1
            count.value = temp


def setup(var):
    global count
    count = var


if __name__ == '__main__':
    myCounter = multiprocessing.Value(ctypes.c_int, 0)
    with concurrent.futures.ProcessPoolExecutor(2,
                                                initializer=setup, initargs=(myCounter,)) as execute:

        t1 = time.perf_counter()
        f1 = execute.submit(counter)
        f2 = execute.submit(counter)
        concurrent.futures.wait([f1, f2],
                                return_when=concurrent.futures.ALL_COMPLETED)
        t2 = time.perf_counter()
        print(myCounter.value)
    print((t2-t1)*1000)
