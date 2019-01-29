import multiprocessing
import time
'''
When we share memory between processes, a situation of chaos can arise when both(or more of) the processes are using the
shared space simultaneously i.e a process starts using the memory when it is already engaged by the other process.
To solve this problem locks are used.
'''


def deposit(balance):
    for i in range(100):
        time.sleep(0.01)
        l.acquire()           # this section of code is called critical section
        balance.value += 1    # the part of code that is accessing the shared resource
        l.release()


def withdrawl(balance):
    for i in range(100):
        time.sleep(0.01)
        l.acquire()
        balance.value -= 1
        l.release()


bal = multiprocessing.Value('i', 0)
l = multiprocessing.Lock()
d = multiprocessing.Process(target=deposit, args=(bal,))
w = multiprocessing.Process(target=withdrawl, args=(bal,))
d.start()
w.start()
d.join()
w.join()
# if we do not use lock above, then we might get values other than 0(the correct result)
print(bal.value)