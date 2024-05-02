# Page 81
import threading
import time


def test():
    while (True):
        time.sleep(0)
        pass


thread1 = threading.Thread(target=test)
thread2 = threading.Thread(target=test)
thread1.start()
thread2.start()
thread1.join()
