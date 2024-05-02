# Page 175
import multiprocessing
import multiprocessing.managers


class MathProxy(multiprocessing.managers.BaseProxy):
    _exposed_ = ('myPi')

    def myPi(self, m, n):
        return self._callmethod('myPi', (m, n))


class myManager(multiprocessing.managers.BaseManager):
    pass


myManager.register("math", proxytype=MathProxy)

if __name__ == '__main__':
    man = myManager(address=("192.168.253.14", 50000), authkey=b"password")
    man.connect()
    math = man.math()
    print(math.myPi(1, 100))
