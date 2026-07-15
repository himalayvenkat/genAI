# pip install pydantic ----> for the pydantic lib to install



from pydantic import BaseModel
from typing import Optional
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


# Pydantic Installation 

# 1. Open cmd  
# C:\Users\XXXX\Documents>mkdir pydantic_project

# C:\Users\XXXX\Documents>cd pydantic_project

# C:\Users\XXXX\Documents\pydantic_project>python -m venv pydantic_venv

# C:\Users\XXXX\Documents\pydantic_project>pydantic_venv\Scripts\activate

# (pydantic_venv) C:\Users\XXXX\Documents\pydantic_project>pip install pydantic

# (pydantic_venv) C:\Users\XXXX\Documents\pydantic_project>python
# Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import pydantic
# >>> print(pydantic.__version__)
# 2.13.4
# >>> exit()

# (pydantic_venv) C:\Users\XXXX\Documents\pydantic_project>deactivate ----> Deactivating virtual env
# C:\Users\XXXX\Documents\pydantic_project>
