import multiprocessing
import time
# multi processing and multi threading are both used to achieve multi tasking
# a process can have multiple threads inside it
# different processes have different address space


def sq(arr):
    global result
    for i in arr:
        time.sleep(0.2)
        result.append(i*i)
        print(i, i*i)
    print('result inside the process p1', result)


def sq2(arr, result2, v, q):   # function to demonstrate process memory sharing
    v.value = 4.5
    for ind, i in enumerate(arr):
        result2[ind] = i*i
        q.put(i*i)
    print(result2[:])


def cube(arr):
    for i in arr:
        time.sleep(0.2)
        print(i, i*i*i)


array = [1, 2, 3, 4, 5, 6]
t = time.time()
result = []
# sq(array)
# cube(array)
# print(time.time() - t) # this took about 2.4 seconds

p1 = multiprocessing.Process(target=sq, args=(array,))
p2 = multiprocessing.Process(target=cube, args=(array,))

p1.start()
p2.start()
p1.join()
p2.join()

print(time.time() - t)  # this took about 1.2 seconds
print('result outside the process p1', result)
# the reason why this is still empty is because every process has a separate address space
# and the process made a copy of result variable for its use


# we can also share memory between processes , this can be achieved by making multiprocessing variables

# below is a multiprocessing array variable
result2 = multiprocessing.Array('i', 6)  # i denotes int data type, 6 is the array size

# a value is also used for sharing memory, but it can accept only one value
v = multiprocessing.Value('d', 0.0)   # 0.0 is the initial value

# we can also use queues for sharing memory among processes
q = multiprocessing.Queue()

p3 = multiprocessing.Process(target=sq2, args=(array, result2, v, q))
p3.start()
p3.join()
print('sharing process memory, result is ', result2[:])
print('v outside the process', v.value)
print('printing from queue')

while not q.empty():
    print(q.get())
