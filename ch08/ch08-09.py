# Page 151
 
import multiprocessing
import multiprocessing.pool


def myFunc(x):
    return x**2


if __name__ == '__main__':
    with multiprocessing.pool.Pool(10) as p:
        results = p.imap(myFunc, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        for result in results:
            print(result)
