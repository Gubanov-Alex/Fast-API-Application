from datetime import datetime
from typing import Optional, Literal
from pydantic import BaseModel, Field, field_validator,HttpUrl, EmailStr
import random


# ==== Metods Pydantic ====
# user = User(name="John", age=30, password="<PASSWORD>")
# print(user.model_dump())
# print(user.model_dump_json(exclude={"password"}))
#
# user2 = User.model_validate({"name": "Jane", "age": 25, "password": "<PASSWORD>"})
# print(user2.model_dump_json())
# ==========================

def generate_random_password()-> str:
    password= ["Password1","<PASSWORD>"]
    return random.choice(password)


class Phone(BaseModel):
    phone: str

class Address(BaseModel):
    country: str
    city: str
    phone: Optional[Phone] = None


class User(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(gt=18, lt=100)
    password: str = Field(default_factory=generate_random_password)
    non_required_field: Optional[str] = None
    address: Optional[list[Address]] = None
    locale: Literal["en", "fr"] = "en"
    created_date: Optional[datetime] = Field(default_factory= datetime.now)
    avatar_url: Optional[HttpUrl] = None
    email: Optional[EmailStr] = None

    @field_validator("password")
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return v


phone = Phone(phone="123456789")
address_1 = Address(country="USA", city="New York", phone=phone)
address_2 = Address(country="UK", city="London")

user = User(name="John",
            age=30, password="<PASSWORD>",
            address=[address_1],
            locale="fr")

user2 = User(age=25,
             name="Jane",
             address=[address_2],
             locale="en",
             avatar_url='https://avatars.githubusercontent.com/u/100003?v=4',
             email= "user@user.com")

user.address.append(address_2)
print(user.model_dump_json())
print(user2.model_dump_json())






