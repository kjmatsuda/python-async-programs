# Page 174
import multiprocessing
import multiprocessing.managers


class SharedListProxy(multiprocessing.managers.BaseProxy):
    _exposed_ = ('getData', 'setData')

    def getData(self):
        return self._callmethod('getData')

    def setData(self, value, index):
        self._callmethod('setData', (value, index))


class myManager(multiprocessing.managers.BaseManager):
    pass


myManager.register("SharedList", proxytype=SharedListProxy)

if __name__ == '__main__':
    man = myManager(address=("192.168.253.14", 50000),
                    authkey=b"password")
    man.connect()
    myList = man.SharedList()
    print(myList.getData())
