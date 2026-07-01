# there are three methods for accessing the base class

# code Duplication
# Explicit call
# super

class Wine:
    def __init__(self,vodka,rum):
        self.vodka = vodka
        self.rum = rum

class Gin(Wine):
    def __init__(self,vodka,rum,water):
        self.vodka = vodka
        self.rum = rum
        self.water = water

x = Gin(50,30,20)
print(x.rum)

# # in the above we will are writing the code again  like
#           self.vodka = vodka
#           self.rum = rum
# By this we are accessing them also its called as code Duplication

# Explicit Method
class Wine1:
    def __init__(self,vodka,rum):
        self.vodka = vodka
        self.rum = rum

class Gin1(Wine1):
    def __init__(self,vodka,rum,water):
        Wine1.__init__(self,vodka,rum)
        self.water = water

x = Gin1(50,24,20)
print(x.rum)

#Super method
class Car:
    def __init__(self,engine,tyres):
        self.engine = engine
        self.tyres = tyres

    def model(self):
        print(f"this is the model {self.engine}")
        

class Alto(Car):
    def __init__(self,engine,tyres,sector):
        super().__init__(engine,tyres) # super will not have self
        self.sector = sector
    
x = Alto("v6",4,"family")
x.model()

    