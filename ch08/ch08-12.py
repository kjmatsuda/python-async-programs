# Page 154
import multiprocessing
import multiprocessing.pool
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
    with multiprocessing.Pool(2, initializer=setup,
                              initargs=(myCounter,)) as p:

        t1 = time.perf_counter()
        asr1 = p.apply_async(counter)
        asr2 = p.apply_async(counter)
        asr1.wait()
        asr2.wait()
        t2 = time.perf_counter()
        print(myCounter.value)
    print((t2-t1)*1000)
