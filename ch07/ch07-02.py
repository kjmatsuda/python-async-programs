# Page 128-129
import multiprocessing
from time import sleep


def addCount(con):
    for i in range(500):
        con.send(i)


def getCount(con, l):
    while True:
        sleep(0.005)
        i = con.recv()
        with l:
            print(i, multiprocessing.current_process().name)


if __name__ == '__main__':

    con1, con2 = multiprocessing.Pipe()
    pLock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=addCount, args=(con1,))
    p2 = multiprocessing.Process(target=getCount, args=(con2, pLock))
    p3 = multiprocessing.Process(target=getCount, args=(con2, pLock))
    p1.start()
    p2.start()
    p3.start()

    p2.join()
