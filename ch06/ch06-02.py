# Page 108
 
import threading
import time

joinLock = threading.Lock()


def myThread1():
    time.sleep(1)
    joinLock.release()


thread1 = threading.Thread(target=myThread1)
joinLock.acquire()
thread1.start()
joinLock.acquire()
