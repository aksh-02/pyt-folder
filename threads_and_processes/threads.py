import threading
import time
# threading improves performance by starting another thread while one thread gets idle(even for a very short time)


def square_func(arr):
    for i in range(len(arr)):
        time.sleep(0.2)
        print(arr[i], arr[i]*arr[i])


def different_square1_func(arr):
    for i in range(0, len(arr), 2):
        time.sleep(0.2)
        print(arr[i], arr[i]*arr[i])


def different_square2_func(arr):
    for i in range(1, len(arr), 2):
        time.sleep(0.2)
        print(arr[i], arr[i]*arr[i])


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
t = time.time()
square_func(array)
print(time.time() - t)

print("now we will use threading")

t1 = threading.Thread(target=different_square1_func, args=(array,))
t2 = threading.Thread(target=different_square2_func, args=(array,))
tn = time.time()
t1.start()
t2.start()
# to wait until both the threads have completed
t1.join()
t2.join()
print(time.time() - tn)