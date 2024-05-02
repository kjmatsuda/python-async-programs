# Page 174-175
 
import multiprocessing
import multiprocessing.managers


class Math:
    def myPi(self, m, n):
        pi = 0
        for k in range(m, n+1):
            s = 1 if k % 2 else -1
            pi += s / (2 * k - 1)
        return pi*4


_math = Math()


def getMath():
    return _math


class MathProxy(multiprocessing.managers.BaseProxy):
    _exposed_ = ("myPi",)

    def myPi(self, m, n):
        return self._callmethod('myPi', m, n)


class myManager(multiprocessing.managers.BaseManager):
    pass


myManager.register("math", callable=getMath, proxytype=MathProxy)

if __name__ == '__main__':
    man = myManager(address=("192.168.253.14", 50000),
                    authkey=b"password")
    s = man.get_server()
    s.serve_forever()
