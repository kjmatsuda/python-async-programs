# Page 165-166
import multiprocessing
import multiprocessing.managers


class Point():
    def __init__(self):
        self._x = 0
        self._y = 0

    def setxy(self, x, y):
        self._x = x
        self._y = y

    def getxy(self):
        return (self._x, self._y)


def myFunc(point):
    point.setxy(42, 43)


class myManager(multiprocessing.managers.BaseManager):
    pass


myManager.register("point", Point)

if __name__ == '__main__':
    man = myManager()
    man.start()
    point = man.point()
    p1 = multiprocessing.Process(target=myFunc, args=(point,))
    p1.start()
    p1.join()
    print(point.getxy())
