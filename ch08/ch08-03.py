# Page 146 
import multiprocessing.pool
import multiprocessing
import random
import time


def myProcess():
    time.sleep(random.randrange(1, 4))
    return multiprocessing.current_process().name


if __name__ == '__main__':
    with multiprocessing.pool.Pool(2) as p:
        asr1 = p.apply_async(myProcess)
        asr2 = p.apply_async(myProcess)
        result1 = asr1.get()
        result2 = asr2.get()
        print(result1, result2)
