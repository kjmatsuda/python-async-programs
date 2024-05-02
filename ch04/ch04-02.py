# Page 74 
import threading


def myThread(sym):
    temp = sym
    while True:
        print(temp)


t1 = threading.Thread(target=myThread, args=("A",))
t2 = threading.Thread(target=myThread, args=("B",))
t1.start()
t2.start()
t1.join()
