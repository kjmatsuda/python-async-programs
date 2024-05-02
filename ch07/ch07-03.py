# Page 131
import time
import multiprocessing
import ctypes


def myUpdate(val):
    for i in range(1000):
        time.sleep(0.005)
        val.value += 1


if __name__ == '__main__':
    myValue = multiprocessing.Value(ctypes.c_int, 0)
    p1 = multiprocessing.Process(target=myUpdate, args=(myValue,))
    p2 = multiprocessing.Process(target=myUpdate, args=(myValue,))
    p2.start()
    p1.start()
    p1.join()
    p2.join()
    print(myValue.value)
