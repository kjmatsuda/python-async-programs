# Page 147
import multiprocessing.pool
import multiprocessing
import random
import time


def myProcess():
    time.sleep(random.randrange(1, 6))
    return multiprocessing.current_process().name


if __name__ == '__main__':
    with multiprocessing.pool.Pool(2) as p:
        asr1 = p.apply_async(myProcess)
        asr2 = p.apply_async(myProcess)

        waiting = True
        while waiting:
            time.sleep(0.01)
            if (asr1.ready()):
                print(asr1.get())
                break
            if (asr2.ready()):
                print(asr2.get())
                break
