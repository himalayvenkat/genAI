# pip install pydantic ----> for the pydantic lib to install



from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

x1 = User(id=1,name='Hima')

print(x1)

# class User1(BaseModel):
#     id: int
#     name: str

# x1 = User1(id='HYHY',name='Hima')

# print(x1)

# o/p ---> Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='HYHY', input_type=str]

# Automatic type converter
class x1(BaseModel):
    age:int
    name:str

xy = x1(age='15',name="Hima")

print(type(xy.age))

# Default Values
class x2(BaseModel):
    age:int = 0
    name:str

xy = x2(name = "Venky")

print(xy)

# optional Feilds
class x3(BaseModel):
    age:int
    name:str
    phone: Optional[str] = None

xy = x3(age = 10,name="Himala")
print(xy)