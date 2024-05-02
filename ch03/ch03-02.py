# Page 52
import multiprocessing


def myProcess():
    while True:
        pass


if __name__ == '__main__':
    p0 = multiprocessing.current_process()
    p1 = multiprocessing.Process(target=myProcess, daemon=True)
    p2 = multiprocessing.Process(target=myProcess, daemon=False)
    p1.start()
    p2.start()
    print(p0.pid)
    print(p1.pid)
    print(p2.pid)
    print("ending")
