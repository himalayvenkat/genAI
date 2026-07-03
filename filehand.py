# to open a file

file = open("order.txt",'w') # if the file is not there then it will create one 

# r'	open for reading (default)
# 'w'	open for writing, truncating the file first
# 'x'	create a new file and open it for writing
# 'a'	open for writing, appending to the end of the file if it exists
# 'b'	binary mode
# 't'	text mode (default)
# '+'	open a disk file for updating (reading and writing)

file.write("Hi this is file handling concept in the python ")

file.close() # closing the file

file = open("order.txt","r")

print(file.read()) # it will gives the o/p of context in the file

file = open("order.txt","r")

print(file.read(10)) # if we want to read 10 chars

file.close()

# read()	Reads the entire file or a specified number of characters
# readline()	Reads one line
# readlines()	Reads all lines into a list
# write()	Writes text to the file
# writelines()	Writes a list of strings to the file
# close()	Closes the file
l1 = ["Hi\n","Welcome\n","Programing\n"]
file = open("order.txt",'w')
file.write("Hi ra Mama.")
file.writelines(l1)
file.close()
file = open("order.txt",'r')
print(file.read())
print("xxxxxxxxxxxxxxx")
print(file.readlines(3))
file.close()

# The with statement automatically closes the file, even if an exception occurs.

with open("x1.txt",'w') as file:
    file.write("Hi ra x1")

file = open('x1.txt')   
print(file.read())

file.close()