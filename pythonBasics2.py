name = "Himalay"
print(type(name))

print(name[0])
print(name[1:])
print(name[::-1]) # It will reverse the string
print(name[0:5:2])# It will print the string from index 0 to 5 with a step of 2


# to store in other languages
name1 = "हिमालय"
print(name1)

email = "Himalay1710@gmail.com"

email1 = email.upper()
email2 = email.lower()
print(f"the Uppercase of the email is  {email1}")
print(f"the Lowercase of the email is  {email2}")

# Title case
name  = "j venkat Himalay"
print(name.title())

# Split the string
name = "Himalay Venkat"
nameSplit = name.split()
print(nameSplit)
print(nameSplit[0])

name = "ven,kat,him,lay"
name = name.split(",")
print(name)

# Finding and replacing a string
name = "Himalay Venkat"
print(name.find("V"))

print(name.replace("V","X"))

# Removing whitvespace
name = "   Himalay Venkat   "
print(name.strip())

name = "HIMALA"
x = "12345"
print(name.isalpha())
print(x.isdigit()) # it will check if the string is a digit or not but it should be a string only


# TUPLES
myTuple = (1,1,1,2,3,4,4,5)# Tuples are immutable which means we cannot change the values of the tuple but we can change the values of the list
print(myTuple)
# Tuples can have duplicates

print(myTuple.count(1))
(spice1,spice2,spice3) = ("salt","pepper","chili") # unpacking the tuple
print(spice2)

a = ("salt","pepper","chili")
b = "pepper" in a
print(b)
b = "pepper1" in a
print(b)

# Lists
# Lists can also have duplicates and they are mutable
l1 = [1,2,3,4,5,6,1]
print(l1)

l1.append(7) # append will add the element at the end of the list
print(l1)

x = l1.pop() # pop will remove the last element of the list and return it
print(x)
print(l1)

# REVERSE A LIST
l1.reverse() # reverse will reverse the list
print(l1)

# Remove in a list
a = ["salt","pepper","chili"]
a.remove("salt")
print(a)

# Sort a list
a = ["salt","pepper","chili"]
a.sort() # sort will sort the list in ascending order
print(a)
a.sort(reverse=True) # sort will sort the list in descending order
print(a)

x = a.count("pepper") # count will count the number of occurrences of the element in the list
print(x)

x = "pepper"
z = x in a
print(z)

# adding two lists
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(l3)

print(l1*3) # it will repeat the list 3 times

# l1*l2 # it will give an error because we cannot multiply two lists but we can multiply a list with an integer

# the objects in the list can not use replace 


####### SETS ###########

# sets will not have duplicates
# sets are represented by curly braces {}
# sets union, intersection, difference, symmetric difference
s1 = {1,2,3,4,5,1}  # it will remove the duplicate value and will only keep one value
print(s1)
s2 = {1,6,7,8,9,2}
print(s2)

# UNION of SETS
s3 = s1.union(s2)
print(s3)

# INTERSECTION of SETS
s4 = s1.intersection(s2)
print(s4)

# DIFFERENCE of SETS
s5 = s1.difference(s2)
print(s5)

# SYMMETRIC DIFFERENCE of SETS
s6 = s1.symmetric_difference(s2)
print(s6)

# Using the symboles for set operations
s7 = s1 | s2 # union
print(s7)

s8 = s1 & s2 # intersection
print(s8)

s9 = s1 - s2 # difference
print(s9)

s10 = s1 ^ s2 # symmetric difference
print(s10)


###### DICTONARIES #########

dict1 = {
    "name": "Himalay",
    "id": 1795,
    "email": "venkathimalay@gmail.com"
}

print(dict1['name'])

dict2 = dict(name = "koushthubham",id=1766,email="koushthubham@gmail.com")
print(dict2)

dict3 = {}

dict3["name"]="pacx"
dict3["email"]="pacx@gmail.com"
dict3["id"]=1222

print(dict3)

print(dict3.keys())
print(dict3.values())
print(dict3.get('id1',"Hi This Key is not there in the Dictionary")) # get will return the value of the key if the key is present in the dictionary otherwise it will return the default value which we have provided as the second argument in the get method

print(dict3.items()) # it will return the key value pairs in the form of a list of tuples

z = dict3.pop("email1","Hi This Key is not there in the Dictionary") # pop will remove the key value pair from the dictionary and return the value of the key if the key is present in the dictionary otherwise it will return the default value which we have provided as the second argument in the pop method
print(z)
# Here in the above line we are trying to pop the key "email1" which is not present in the dictionary so it will return the default value which we have provided as the second argument in the pop method

z1 = dict3.popitem() # popitem will remove the last key value pair from the dictionary and return it as a tuple
print(z1)
print(dict3)
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
dict3.update(dict1) #
print(dict3)

a = {"name": "Himalay"}
b = {"name": "Himalayb"}
c = {"name": "HimalayC"}
d = {"hin":"huhu"}

a.update(b)
print(a)

a.update(d)
print(a)

import arrow
print(arrow.now())

# Datetime modules , time delta modules,arrow,date utils modules
