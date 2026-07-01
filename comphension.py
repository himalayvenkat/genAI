# comphension is also like  inheritance 
# like a son will inherit the property of the dad
# here init is constructor

class Chai:
    def __init__(self,hot,extraIng):
        self.hot = hot
        self.extraIng = extraIng

    def teaTime(self):
        print(f"Hi Its the Tea time with {self.extraIng}")

class masala:
    c1 = Chai(True,"Elachi")
    def __init__(self,ing1):
        self.ing1 = ing1


x = masala("Cardomom")
x.c1.teaTime() # its the composition
