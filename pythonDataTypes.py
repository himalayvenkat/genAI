# integer
x = 15
print(x)
print(type(x))

y = -3
print(type(y))
# Float
a = 2.00
print(type(a))

b = 2+3j
print(type(b))
# boolean
a = True
print(type(a))

b = False
print(type(b))

# Mathematical operations
x = 10
y = 3
print(x+y)
print(x-y)
print(x*y)
print(x/y) # division always returns a float
print(x%y) # modulus operator returns the remainder of the division
print(x//y) # floor division returns the quotient without the remainder
print(x**y) # exponentiation operator returns x raised to the power of y

# Complex operations
a = 2+3j
b = 5+10j
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b) # exponentiation of complex numbers is more complex and involves using Euler's formula, but it can be calculated using the built-in complex number functions in Python.
print(a.real) # returns the real part of a, which is 2.0
print(a.imag) # returns the imaginary part of a, which is 3.0
print(a.conjugate())  # returns the complex conjugate of a, which is 2-3j


# to do some of the operations we will import the math module
import cmath as c # cmath module is used for complex numbers
import math as m # math module is used for real numbers
a = 100
b =25
print(m.sqrt(a))
print(m.factorial(b))

x1 = 8+10j
print(c.sqrt(x1))

