# Page 168-169
import multiprocessing
import multiprocessing.managers


class Counter():
    def __init__(self):
        self.myCounter = 0

    def getCount(self):
        return self.myCounter

    def setCount(self, value):
        self.myCounter = value
    count = property(getCount, setCount)


class CounterProxy(multiprocessing.managers.BaseProxy):
    _exposed_ = ('getCount', 'setCount')

    def get(self):
        return self._callmethod('getCount')

    def set(self, value):
        return self._callmethod('setCount', (value,))
    value = property(get, set)


class myManager(multiprocessing.managers.BaseManager):
    pass


myManager.register("counter", callable=Counter,
                   proxytype=CounterProxy)


def count(myCounter):
    for i in range(1000):
        myCounter.value = myCounter.value+1


if __name__ == '__main__':
    man = myManager()
    man.start()
    counter = man.counter()

    p1 = multiprocessing.Process(target=count, args=(counter,))
    p2 = multiprocessing.Process(target=count, args=(counter,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(counter.value)
