class Voter:
    def __init__(self,age):
        self._age = age

    @property 
    # the property is used for the getter
    def age(self):
        return self._age+2
    
    @age.setter
    def setAge(self,age):
        if 2<=age<=5:
            self._age = age
        else:
            raise ValueError("The age is less")
        
x = Voter(3)
y = x.age
x.setAge = 0
