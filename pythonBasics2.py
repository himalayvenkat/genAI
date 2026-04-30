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

