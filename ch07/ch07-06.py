# Page 138
 
import time
import multiprocessing
import multiprocessing.shared_memory


def myUpdate(mySharedList, lock):
    for i in range(1000):
        time.sleep(0.005)
        with lock:
            mySharedList[0] = mySharedList[0]+1
    mySharedList.shm.close()


if __name__ == '__main__':
    mylock = multiprocessing.Lock()
    mySharedList = multiprocessing.shared_memory.ShareableList(
        sequence=[1])
    p1 = multiprocessing.Process(target=myUpdate,
                                 args=(mySharedList, mylock))
    p2 = multiprocessing.Process(target=myUpdate,
                                 args=(mySharedList, mylock))
    p2.start()
    p1.start()
    p1.join()
    p2.join()
    print(mySharedList[0])
    mySharedList.shm.close()
    mySharedList.shm.unlink()
