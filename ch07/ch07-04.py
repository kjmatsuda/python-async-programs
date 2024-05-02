# Page 135 
import time
import multiprocessing
import multiprocessing.shared_memory


def myUpdate(name, lock):
    mySharedMem = multiprocessing.shared_memory.SharedMemory(
        create=False, name=name)
    for i in range(127):
        time.sleep(0.005)
        with lock:
            mySharedMem.buf[0] = mySharedMem.buf[0]+1
    mySharedMem.close()


if __name__ == '__main__':
    mylock = multiprocessing.Lock()
    mySharedMem = multiprocessing.shared_memory.SharedMemory(
        create=True, size=10)
    mySharedMem.buf[0] = 1
    p1 = multiprocessing.Process(target=myUpdate,
                                 args=(mySharedMem.name, mylock))
    p2 = multiprocessing.Process(target=myUpdate,
                                 args=(mySharedMem.name, mylock))
    p2.start()
    p1.start()
    p1.join()
    p2.join()
    print(mySharedMem.buf[0])
    mySharedMem.close()
    mySharedMem.unlink()
