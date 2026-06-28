# generators 

# they are nothing but functions

# why we will use generators means 
# 1. we will save memory
# 2. lazy evaluation
# 3. we dont want the results immediatly

def chai():
    yield("Chai 1")
    yield("Chai 2")
    yield("Chai 3")
    yield("Chai 4")

print(chai()) # ===> This will give th o/p <generator object chai at 0x000001EE83168F60>

x = chai()
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# infinite generators mostly used in the AI , Mostly it will have a never ending loop
# mostly used in the strams , real time data

def inf_chai():
    count = 1
    while True:
        yield(f"the order no {count}")
        count += 1

us1 = inf_chai()
us2 = inf_chai()
for i in range(6):
    print(next(us1))
for i in range(3):
    print(next(us2))


# Sending Values to the Yield
# we will send values bu using order = yield


def chai():
    print("Welcome to chai")
    order = yield
    while True:
        print(f" your order of {order} is ready")
        order = yield

stall = chai()
next(stall)
stall.send("Masala chai")


# decorators is like a wrapper for the gift
# and gift is the actual function

def my_decorotors(func):
    def wrapper():
        print("Before function")
        func()
        print("after function")
    return wrapper


@my_decorotors
def greet():
    print("HI Bro this is the original code")
    return None


greet()

print(greet.__name__) # here it is the wrapper but when we try it has to show the Greet as the name of the function so for that we need to do some changes as shown below

from functools import wraps

def my_decorotors(func):
    @wraps(func)
    def wrapper():
        print("Before function")
        func()
        print("after function")
    return wrapper


@my_decorotors
def greet():
    print("HI Bro this is the original code")
    return None


greet()

print(greet.__name__) # ====> now it will show greet



# logging Decorator
from functools import wraps
def log_decorator(func):
    @wraps(func)
    def wrapper(*args):
        print("Befor function")
        func(*args)
        print("after function")
    return wrapper

@log_decorator
def logfunc(type):
    print(f"Hi this is logging decoration, but we are passing a argument with type as {type}")

logfunc("Masala")

# Authorization in decorators
from functools import wraps
def auth_decorator(func):
    @wraps(func)
    def wrapper(user):
        print("before function")
        if user == "developer":
            print("access not granted contact admin")
        else:
            func(user)
        print("after function")
    return wrapper
        

@auth_decorator
def auth(user):
    print("access granted")

auth('admin')
auth('developer')

