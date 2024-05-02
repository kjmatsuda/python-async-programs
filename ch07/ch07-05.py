# Page 136
 
import time
import multiprocessing
import multiprocessing.shared_memory
import sys


def myUpdate(mySharedMem, lock):
    for i in range(1000):
        time.sleep(0.005)
        with lock:
            count = int.from_bytes(
                mySharedMem.buf[0:8], byteorder=sys.byteorder)
            count = count+1
            mySharedMem.buf[0:8] = int.to_bytes(
                count, 8, byteorder=sys.byteorder)
    mySharedMem.close()


if __name__ == '__main__':
    mylock = multiprocessing.Lock()
    mySharedMem = multiprocessing.shared_memory.SharedMemory(
        create=True, size=10)
    mySharedMem.buf[0:8] = int.to_bytes(1, 8,
                                        byteorder=sys.byteorder)
    p1 = multiprocessing.Process(target=myUpdate,
                                 args=(mySharedMem, mylock))
    p2 = multiprocessing.Process(target=myUpdate,
                                 args=(mySharedMem, mylock))
    p2.start()
    p1.start()
    p1.join()
    p2.join()
    count = count = int.from_bytes(mySharedMem.buf[0:8],
                                   byteorder=sys.byteorder)
    print(count)
    mySharedMem.close()
    mySharedMem.unlink()
