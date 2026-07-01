# mro means method resolution order ,Its nothing but multiple inheritance 

# A ->B
# A ->C 
# B,C ->D 

# Code example

class A:
    label = "A class"

class B(A):
    label = "B class"

class C(A):
    label = "C class"

class D(B,C):
    #label = "D class"
    pass

x = D()
print(x.label) 

# class D(B,C): as B is given at first so it will print the Bclass as the output
# class D(C,B): as B is given at first so it will print the Cclass as the output
