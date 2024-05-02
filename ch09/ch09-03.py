# Page 162
import multiprocessing


def count(myCounter):
    for i in range(1000):
        myCounter.value = myCounter.value+1


if __name__ == '__main__':
    man = multiprocessing.Manager()
    counter = man.Value(int, 0)

    p1 = multiprocessing.Process(target=count, args=(counter,))
    p2 = multiprocessing.Process(target=count, args=(counter,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(counter.value)
