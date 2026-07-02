class Mathsyl:
    math_teacher = "Sinu"

    def __init__(self,a,b):
        self.a = a
        self.b = b

    @classmethod
    def add (cls,new_math_teacher):
        cls.math_teacher = new_math_teacher
        return cls.math_teacher

x = Mathsyl(4,5)
print(Mathsyl.math_teacher)
print(x.add("hima"))
print(Mathsyl.math_teacher)