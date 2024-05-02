# Page 77
import threading

myObject = threading.local()


def myThread(sym):
    myObject.temp = sym
    while True:
        print(myObject.temp)


t1 = threading.Thread(target=myThread, args=("A",))
t2 = threading.Thread(target=myThread, args=("B",))
t1.start()
t2.start()
t1.join()
