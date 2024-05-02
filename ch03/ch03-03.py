# Page 55
import multiprocessing
import multiprocessing.connection
import random
import time


def myProcess():
    time.sleep(random.randrange(1, 4))


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=myProcess)
    p2 = multiprocessing.Process(target=myProcess)
    p3 = multiprocessing.Process(target=myProcess)
    p1.start()
    p2.start()
    p3.start()

    waitList = [p1.sentinel, p2.sentinel, p3.sentinel]
    res = multiprocessing.connection.wait(waitList)
    print(res)
    print(waitList.index(res[0])+1)
