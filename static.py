class Acadamy:
    school_name = "Jangati"

    def __init__(self,name,age):
        self.name = name
        self.age = age

# static method will not have the "self" argument 

    @staticmethod
    def pakodi():
        print("this is pakodi")

x1 = Acadamy("himalay",15)
x1.pakodi()


