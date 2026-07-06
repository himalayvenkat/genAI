
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


