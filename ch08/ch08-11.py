# Page 153
import functools
import multiprocessing
import multiprocessing.pool


def myFunc(x):
    return x**2


def mySum(value, item):
    return value+item


if __name__ == '__main__':
    with multiprocessing.pool.Pool(10) as p:
        asr = p.map_async(myFunc, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        res = asr.get()
    sumsquares = functools.reduce(mySum, res)
    print(sumsquares)
