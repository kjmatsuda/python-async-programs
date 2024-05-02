# Page 107
 
import threading
import time


def myThread1():
    time.sleep(1)
    thread2.join()


def myThread2():
    time.sleep(1)
    thread1.join()


thread1 = threading.Thread(target=myThread1)
thread2 = threading.Thread(target=myThread2)
thread1.start()
thread2.start()
