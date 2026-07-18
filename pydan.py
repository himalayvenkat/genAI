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

from pydantic import BaseModel

class U1(BaseModel):
    id:int
    name:str
    price:float
    in_stock:bool

data = {
    'id':101,
    'name':"Laptop",
    'price':120, # its a int , but it will give float
    'in_stock': 'true' # it will automatically convert but we should not give it
}

x = U1(**data)
print(x) # o/p = id=101 name='Laptop' price=120.0 in_stock=True
print(x.name) # o/p = Laptop

from typing import List,Dict,Optional
from pydantic import BaseModel,Field
import re
class B1(BaseModel):
    id: int
    name: str
    subjects: List[str] = ['Eng','Hindi','Telugu']
    age: int = Field(
        ...,
        ge = 15,
        lt =25
    )
    marks: Dict[str,float]
    place: Optional[str] = 'HYD'

data = {
    'id': 101,
    'name': 'Hima',
    'subjects': ['Maths','Eng','Telugu'],
    'age': 20,
    'marks': {
        'Maths': 100,
        'Eng': 80,
        'Telugu': 100
    }
}
xx = B1(**data)
print(xx)

class B2(BaseModel):
    id: int
    name: str
    email : str = Field(
        ...,
        min_length = 3,
        max_length = 50,
        pattern = r'^[A-Za-z0-9._%+-]+@gmail.com'
    )
    
data1 = {
    'id': 101,
    'name': 'Hima',
    'email': 'himalay@gmail.com'
}

xy1 = B2(**data1)
print(xy1)

# Field Validator


### this is an error program 
# from pydantic import BaseModel,field_validator
# class U1(BaseModel):
#     username: str
#     password: str

#     @field_validator('username')
#     def use(cls,v):
#         if(len(v)<4):
#             raise ValueError("Min length >4")
#         return v
# data = {'username': "Hi",'password':"GTGT"}   
# x = U1(**data)
# print(x)


## its an error
# from pydantic import BaseModel,field_validator
# class U11(BaseModel):
#     username: str
#     password: str

#     @field_validator('username','password')
#     def cdc(cls,v):
#         if (len(v)<4):
#             raise ValueError("Its an error")
#         return v

# x = U11(username ="HIHIH",password='HUH')

from pydantic import BaseModel,field_validator
class U12(BaseModel):
    username: str
    password: str

    @field_validator('username')
    def x1(cls,v):
        if (len(v)<4):
            raise ValueError('Hi its an error of one')
        return v
xx = U12(username = 'HIHIHI',password = 'JUJUJU')    
print(xx)

from pydantic import BaseModel,model_validator
class U13(BaseModel):
    username: str
    password: str

    @model_validator(mode = 'after')
    # the below one is depricated
    def cec(cls,values):
        if (values.username == values.password):
            raise ValueError("Username and password can not be same")
        return values
# x = U13(username = 'HIHIHI',password = "HIHIHI") ---> This will give error
x = U13(username = 'HIHIHIUHU',password = "HIHIHI")
print(x)


from pydantic import BaseModel,model_validator
class U13(BaseModel):
    username: str
    password: str

    @model_validator(mode = 'after')
    # instance 
    def cec(self):
        if (self.username == self.password):
            raise ValueError("Username and password can not be same")
        return self
# x = U13(username = 'HIHIHI',password = "HIHIHI") ---> This will give error
x = U13(username = 'HIHIHIUHU',password = "HIHIHI")
print(x)

from pydantic import BaseModel,Field,computed_field
class book(BaseModel):
    id: int
    roomid: int
    rate : int
    days: int = Field(
        ...,
        ge =1
    )

    @computed_field
    @property
    def totalBill(self)-> float:
        return self.rate*self.days
    
x = book(id = 1,roomid = 123,rate = 1000,days = 5)

print(x)
print(x.model_dump())
print(x.totalBill)
from typing import Annotated
from pydantic import BaseModel,field_validator,model_validator,BeforeValidator


def priceConvert(value):
        if '$' in value:
            value.replace('$','')
        elif ',' in value:
            value.replace(',','')
        return value


class u111(BaseModel):
    id: int
    name: str
    email : str
    price: Annotated[str,BeforeValidator(priceConvert)]

    @field_validator('id')
    def idValue(cls,v):
        if (v>100):
            raise ValueError('The id value can not be greater than 100')
        return v
    
    @model_validator(mode = 'before')
    @classmethod
    def valCheck(self,values):
        if values["id"] <10 and len(values["email"])<5:
            raise ValueError('The ID is less than 10 and the email length is less than 5')
        return values

    
x = u111(id = 30,name = 'Himalay',email = 'Himalay@gmail.com',price='$5.44')

print(x)

from typing import Annotated
from pydantic import BaseModel,BeforeValidator,AfterValidator


def check1(value):
    print(value)
    print('check pass1')
    return value

def check2(value):
    print(value)
    print('pass2')
    return value

class U32(BaseModel):
    id: int
    name: str
    email: Annotated[str,BeforeValidator(check1)]
    Pass: Annotated[str,AfterValidator(check2)]

x = U32(id=123,name="Hima",email = "Emails@gmail.com",Pass = "Gygy")
print(x)


from typing import List,Optional
from pydantic import BaseModel

class U11(BaseModel):
    id: str
    name: str
    relationU11: Optional[List['U11']]=None

U11.model_rebuild()
x = U11(id = '1',name='sgtg',relationU11 = [U11(id = '1.1',name = "Pakodi"),U11(id = '1.2',name = "Kodi"),U11(id = '1.3',name = "Pakodi123",relationU11 = [U11(id = '1.3.1',name = "Kodi")])])
print(x)

from typing import Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    lane_no: Optional[str]=None
    PIN: int

class User(BaseModel):
    id: int
    name: str
    address : Address

data = {
    'id' : 1,
    'name' : "Himalay",
    'address': {
        'street' : "st111",
        'PIN': 500056
    }
}

x = User(**data)
print(x)

