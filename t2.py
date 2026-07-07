
import threading

# Its the main thread
print(threading.current_thread()) # <_MainThread(MainThread, started 24072)>

def work1(a,b):
    print(a+b)
    print(threading.current_thread().name) # it will give AddThread as name
    return a+b

t1 = threading.Thread(target=work1,args=(5,10),name="addThread")

# "print(t1.start())" This command will always give none , Threads wont print

t1.start()
print(threading.current_thread().name) # it will give you mainThread only , as we are calling the finction so inside function it will new name
t1.join()

# Daemon thread
import time

def work22():
    while True:
        print("Running")
        time.sleep(1)
t2 = threading.Thread(target=work22)
t2.daemon = True
t2.start()
# t2.join() as we should not mention this as the main thread waits, and the junior thread wont complete
print("Main thread finished")


# Rule to remember
# daemon=True does not stop a thread immediately.
# It only tells Python:
# "When the program is exiting, don't wait for this thread."
# join() always waits for the thread to finish. If the thread never finishes (like while True), join() blocks forever, regardless of whether the thread is a daemon or not.

count = 100

def w1():
    global count
    for i in range(1,10):
        count += 1
        print(count,f" with thread {threading.current_thread().name}")
    
t1 = threading.Thread(target=w1,name="W1")
t2 = threading.Thread(target=w1,name="W2")

t1.start()
t2.start()

t1.join()
t2.join()




count = 100
lock = threading.Lock()

def w1():
    global count
    lock.acquire()
    for i in range(1,10):
        count += 1
        print(count,f" with thread {threading.current_thread().name}")
    lock.release()
t1 = threading.Thread(target=w1,name="W1")
t2 = threading.Thread(target=w1,name="W2")

t1.start()
t2.start()

t1.join()
t2.join()


# Rlock:

# it allows the same thread to acquire the lock multiple times without blocking itself.
import threading
# lock = threading.Lock() ---> It will give error see the reason below
lock = threading.RLock()

def f1():
    lock.acquire()
    print('inside the f1')
    lock.release()

def f2():
    lock.acquire()
    print('inside f2')
    f1()
    lock.release()

t1 = threading.Thread(target=f2)
t1.start()
t1.join()

# the function is stopped because , lock is not closed and then we are going to another lock
# so to make it best we need to use the RLock -> Reentrant Lock

# Semaphore
# it allows a fixed number of threads to run the resource at a time 

import threading
import time

s = threading.Semaphore(3)

def w1():
    with s:
        print(threading.current_thread().name, "started")
        time.sleep(2)
        print(threading.current_thread().name, "finished")

for i in range(5):
    threading.Thread(target=w1).start()

# Output: if you observe the first three were executed stright, because of the   s = threading.Semaphore(3) 

# Thread-1 (w1) started
# Thread-2 (w1) started
# Thread-3 (w1) started
# Thread-1 (w1) finished
# Thread-2 (w1) finished
# Thread-3 (w1) finished
# Thread-4 (w1) started
# Thread-5 (w1) started
# Thread-4 (w1) finished
# Thread-5 (w1) finished


# Event is used for the communication of other threads

import threading
event = threading.Event()

def w1():
    print('event waiting')
    event.wait()
    print('started')

t1 = threading.Thread(target=w1)
t1.start()
input('press enter')
event.set()


