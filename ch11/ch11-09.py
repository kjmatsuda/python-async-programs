# Page 207
import concurrent.futures
import time


def taskA():
    time.sleep(1)
    ans = f2.result()
    return ans


def taskB():
    time.sleep(1)
    ans = f1.result()
    return ans


with concurrent.futures.ThreadPoolExecutor(2) as execute:
    f1 = execute.submit(taskA)
    f2 = execute.submit(taskB)
    concurrent.futures.wait([f1, f2],
                            return_when=concurrent.futures.ALL_COMPLETED)
    print(f1.result())
