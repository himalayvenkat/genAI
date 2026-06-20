# function

def add (a,b):
    return a+b

print(add(5,10))

def sub(a,b):
    return a-b

a1 = sub(10,5)
print(a1)

def norm():
    print("Hi i am inside the function")

norm()

# Parameters

def x1(a,b): 
    c = a*b
    print(c)
    # here a,b ate the parameters

x1(5,10) 
# in the above line 5,10 are the arguments

def addVat(price,varRate):
    return price+((varRate/100)*price)

orders = [100,150,120]
for i in orders:
    bill = addVat(i,10)
    # here bill is the local varable in side the function
    print(bill)

# nested functions
def update_order():
    chai_type = "Elachi"
    def kitchen():
        nonlocal chai_type # here we are using nonlocal because the chai type
        chai_type = "Masala"
    kitchen()
    print(chai_type)

update_order()

x = "masala"

def up():
    global x
    x = "elachi"
    print(x)

up()


##### Observe this Fuction
def splChai(*ing,**extras):
    print("ingridents",ing)
    print("extras",extras)

splChai("masala","elachi",sweet = "Honey",hot="Yes")

# Return multiple values

def retVal():
    return 100,200,300

x,y,z= retVal()

print(x)
print(y)
print(z)

def retVal():
    return 100,200,300,400,500

x,y,z,_,_= retVal()

print(x)
print(y)
print(z)

# Lambda Fuction

chai_type = ['light','kadak','ginger','k1']
strong_chai =list(filter(lambda i:i!="kadak",chai_type))
print(strong_chai)

