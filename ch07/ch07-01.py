# Page 125
import multiprocessing


def addCount(q):
    for i in range(1000):
        q.put(i)


def getCount(q, l):
    while True:
        i = q.get()
        with l:
            print(i)


if __name__ == '__main__':
    q = multiprocessing.Queue()
    pLock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=addCount, args=(q,))
    p2 = multiprocessing.Process(target=getCount, args=(q, pLock))
    p3 = multiprocessing.Process(target=getCount, args=(q, pLock))
    p1.start()
    p2.start()
    p3.start()

    p3.join()
