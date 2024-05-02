# Page 75
import threading


def myThread(sym):
    myThread.temp = sym
    while True:
        print(myThread.temp)


myThread.temp = ""

t1 = threading.Thread(target=myThread, args=("A",))
t2 = threading.Thread(target=myThread, args=("B",))
t1.start()
t2.start()
t1.join()
