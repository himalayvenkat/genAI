# inheritance is nothing but inheritance 
# like a son will inherit the property of the dad
# here init is constructor

class Chai:
    def __init__(self,hot,extraIng):
        self.hot = hot
        self.extraIng = extraIng

    def teaTime(self):
        print(f"Hi Its the Tea time with {self.extraIng}")

class masala(Chai):
    def __init__(self,hot,extraIng,ing1):
        self.hot = hot
        self.extraIng = extraIng
        self.ing1 = ing1

# here x is the object for the masala but its the inherited from the chai class
x = masala(True,"Elachi","Cardomom")

x.teaTime()
