class Car:
    wheels = 4
    body="steel"

suzuki = Car()

suzuki.color = "red"

print(Car.wheels)
print(Car.body)
print(suzuki.color)
print(suzuki.body)

# now changing the properties of the suzuki body
suzuki.body = "Stainless Steel"

print(suzuki.body)

del suzuki.body # we are deleting the body , But when we print it it will give ypu the steel , this is called as attribute shodowing
print(suzuki.body)

# now we will delete the properties of the class itself

del Car.body
# print(suzuki.body) # this will sow the error
