import multiprocessing
import time
# we can divide a work between all the cores of the cpu while usually it's done on a single core
# this is achieved using a pool
# 'map' divides the work and 'reduce' accumulates the result


def f(i):
    a = 0
    for z in range(100):
        a += z*z
    return a


if __name__ == "__main__":
    result1 = []
    t1 = time.time()
    for k in range(10000):
        result1.append(f(k))
    print(result1)
    print(time.time() - t1)

    # now let's do it by using all the cores on the cpu using a multiprocessing pool
    t2 = time.time()
    p = multiprocessing.Pool(processes=3)  # creates 3 processes
    result2 = p.map(f, range(10000))    # to divide the input of the function between all the cores
    p.close()
    p.join()
    print(result2)
    print(time.time() - t2)
