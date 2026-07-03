x = 10
y = 20
z = '3x'

# raise and except work only with classes that inherit from Python's built-in Exception class.
# so thats why we are mentioning Exception in the token error class

class tokenError(Exception): pass
try:
    if x+y == 50:
        print("No error")
    else:
        raise tokenError ("Hi man you have raised an error") 
except tokenError as e:
    print('Error:',e)


class Voter:
    def __init__(self,age):
        self.age = age
    
    def verification(self):
        try:
            if self.age >18:
                print("Eligible for voting")
            else:
                xError = {
                    'errorCode': 400,
                    'errorMsg':"Not eligible"
                }
                raise tokenError(xError)
        except tokenError as e:
            print(e)

x = Voter(15)
x.verification()
    
# this above one has the try & except in the class but its a good way to write it outside the class

class Voter:
    def __init__(self,age):
        self.age = age
    
    def verification(self):
            if self.age >18:
                print("Eligible for voting")
            else:
                xError = {
                    'errorCode': 400,
                    'errorMsg':"Not eligible"
                }
                raise tokenError(xError)

try:
    x = Voter(15)
    x.verification()
except tokenError as e:
    print(e)
