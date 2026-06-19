# For Loop using Range
# loops will always have the exclude the max  range(1,11) means it will only take 10
for i in range(1,11):
    print(i)

# loops in List 

a = [1,2,3,4,5,6,7,8,9,10]
for i in a:
    print(i)

b = ["Ram","ROM","MAX","DELIC"]
for i in b:
    print(i)

# While Loop 
a = 1
while a<10:
    print(a)
    a+=1

# Task Preparing chai tokens
for token in range (1,11):
    print(f"the token for the chai is {token}")

#Enumerate Function is used to print with the index value or the numbering you want

a = ["Ram","sham","pari","karan"]
print(list(enumerate(a)))
# the output is [(0, 'Ram'), (1, 'sham'), (2, 'pari'), (3, 'karan')]

# if we want to start with i Then
print(list(enumerate(a,start=1)))
print((enumerate(a,start=1))) # This is the output for this <enumerate object at 0x00000166BABD7CE0>

for i,j in enumerate(a,start=1):
    print(f"{i}:{j}")
# The output is 
# 1:Ram
# 2:sham
# 3:pari
# 4:karan

l1 = ["a","b","c","d","e"]
b = [100,200,300,400,500]
for item in zip(l1,b):
    print(item)
# The output
# ('a', 100)
# ('b', 200)
# ('c', 300)
# ('d', 400)
# ('e', 500)

# Continue will make the iteration will be move to next one
# Break will stip the loop 

a = ["hi","ra","pa","ma","ka"]

for i in a:
    if i == "pa":
        print(f"{i} in continue flow")
        continue
    elif i=="ma":
        break
    print(i) 

# for else operator
a = []
for i in a:
    if i == "Hi":
        print(i)
else:
    print("its Null")

a = ["pi"]
for i in a:
    if i == "Hi":
        print(i)
else:
    print("its Null")

# Warlus operator
# its a combination of the assinment and expression
# y:=a%5 =====> as we did not defined Y previously but its not showing any error
a = 5000
if y:=a%5 ==0:
    print("Boola")


