# Page 145 
import multiprocessing.pool
import multiprocessing
import random
import time


def myProcess():
    time.sleep(random.randrange(1, 4))
    return multiprocessing.current_process().name


def myCallback(result):
    print(result)


if __name__ == '__main__':
    p = multiprocessing.pool.Pool(2)
    p.apply_async(myProcess, callback=myCallback)
    p.apply_async(myProcess, callback=myCallback)
    p.close()
    p.join()
