# Page 49
import multiprocessing


def myProcess():
    print("Hello Process World")


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=myProcess)
    p1.start()
 
