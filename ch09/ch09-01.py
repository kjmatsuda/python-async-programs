# Page 160
import multiprocessing
import multiprocessing.pool
import time


def myFunc(x):
    for i in range(len(x)):
        x[i] = x[i]**2


if __name__ == '__main__':
    man = multiprocessing.Manager()
    myList = man.list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    p = multiprocessing.Process(target=myFunc, args=(myList,))
    t1 = time.perf_counter()
    p.start()
    p.join()
    t2 = time.perf_counter()

    print((t2-t1)*1000)
    print(myList)
