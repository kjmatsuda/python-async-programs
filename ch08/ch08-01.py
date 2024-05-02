# Page 144
 
import multiprocessing.pool
import multiprocessing
import random
import time


def myProcess():
    time.sleep(random.randrange(1, 4))
    print(multiprocessing.current_process().name)


if __name__ == '__main__':
    p = multiprocessing.pool.Pool(2)
    p.apply_async(myProcess)
    p.apply_async(myProcess)
    p.close()
    p.join()
