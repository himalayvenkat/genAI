# threading Basics

import threading
import time

def work1():
    print("This is work 1")

def work2():
    print("this is work2")
    time.sleep(10)
    # the time.sleep makes the function sleep for the 10 seconds


t1 = threading.Thread(target=work1)
t5 = threading.Thread(target=work2)
t2 = threading.Thread(target=work1)
t3 = threading.Thread(target=work1)
t4 = threading.Thread(target=work1)


t1.start()
t5.start()
t2.start()
t3.start()
t4.start()



t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
