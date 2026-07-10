import multiprocessing

def worker():
    print("its a multi processing")

if __name__ == "__main__":
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()


# with args,
import multiprocessing

def x1(a):
    print(f'hi ra mama {a}')

if __name__ == '__main__':
    p = multiprocessing.Process(target = x1,args=('Himalay',))

    p.start()
    p.join()
    print("Process completed")

# current Process Name
import multiprocessing
def x2():
    print(multiprocessing.current_process().name)

if __name__ == '__main__':
    p = multiprocessing.Process(target=x2,name = "Pakodi")

    p.start()
    p.join()
    print("Process completed")

# passing arguments

import multiprocessing
def x3(a,b):
    print(a+b)

if __name__ == '__main__':
    p = multiprocessing.Process(target=x3,args=(2,3))
    # But when string is passed we need to pass it like this agrs = ("A",)
    p.start()
    p.join()

# Daemon thread
# as it means it should not have join as it will turminates automatically when the main process executes

import multiprocessing
def x4():
    while True:
        print("Process is Running")

if __name__ == '__main__':
    p = multiprocessing.Process(target=x4)
    p.daemon = True
    p.start()
    print("Main ends")

# returning values:

# Processes do not return values like normal function calls because each process has its own memory.

# Instead, use a Queue or Pipe.

import multiprocessing
def x4(n,q):
    q.put(n*n)

if __name__ == '__main__':
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=x4,args=(5,q))

    p.start()
    print(q.get())
    p.join()

# pipe
import multiprocessing
def x5(a):
    a.send("Hello")
    a.close()
if __name__=='__main__':
    b,c = multiprocessing.Pipe() 
    p = multiprocessing.Process(target=x5,args=(c,))
    p.start()
    print(b.recv())
    p.join()

# Value
import multiprocessing
def incr(x):
    x.value += 10
    print(x.value)

if __name__ == '__main__':
    num = multiprocessing.Value('i',5)
    p = multiprocessing.Process(target=incr,args=(num,))
    p.start()
    p.join()
    print(num.value)

# array

import multiprocessing
def incr(x):
    x[0] += 10
    x[1] +=100
    print(x[:])

if __name__ == '__main__':
    num = multiprocessing.Array('i',[10,20,30,40])
    p = multiprocessing.Process(target=incr,args=(num,))
    p.start()
    p.join()
    print(num[:])