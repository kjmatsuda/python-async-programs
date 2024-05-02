# Page 91
import multiprocessing
import time


def myProcess(lock):
    lock.acquire()
    time.sleep(4)
    lock.release()


if __name__ == '__main__':
    myLock = multiprocessing.Lock()
    p1 = multiprocessing.Process(target=myProcess, args=(myLock,))
    p2 = multiprocessing.Process(target=myProcess, args=(myLock,))
    t1 = time.perf_counter()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    t2 = time.perf_counter()
    print((t2-t1)*1000)
