# Page 206
import concurrent.futures
import multiprocessing
import multiprocessing.managers
import time
import ctypes


def counter(count, lock):
    for i in range(10000):
        with lock:
            temp = count.value+1
            count.value = temp


if __name__ == '__main__':

    with multiprocessing.Manager() as man:
        with concurrent.futures.ProcessPoolExecutor(2) as execute:

            myCounter = man.Value(ctypes.c_int, 0)
            myLock = man.Lock()

            t1 = time.perf_counter()
            f1 = execute.submit(counter, myCounter, myLock)
            f2 = execute.submit(counter, myCounter, myLock)
            concurrent.futures.wait([f1, f2],
                                    return_when=concurrent.futures.ALL_COMPLETED)
            t2 = time.perf_counter()
            print(myCounter.value)
    print((t2-t1)*1000)
