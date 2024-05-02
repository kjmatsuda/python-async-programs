# Page 172
import multiprocessing
import multiprocessing.managers


class SharedList():
    def __init__(self):
        self.list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def getData(self):
        return self.list

    def setData(self, value, index):
        self.list[index] = value


class SharedListProxy(multiprocessing.managers.BaseProxy):
    _exposed_ = ('getData', 'setData')

    def getData(self):
        return self._callmethod('getData')

    def setData(self, value, index):
        self._callmethod('setData', (value, index))


_sharedList = SharedList()


def SharedList():
    return _sharedList


class myManager(multiprocessing.managers.BaseManager):
    pass


myManager.register("SharedList", callable=SharedList,
                   proxytype=SharedListProxy)

if __name__ == '__main__':
    man = myManager(address=("192.168.253.14", 50000), authkey=b"password")
    s = man.get_server()
    s.serve_forever()
