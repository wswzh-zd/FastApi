from fastapi import APIRouter, UploadFile
from pydantic import BaseModel, EmailStr
from datetime import date
from typing import List,Union
from fastapi import Request

class UserIn(BaseModel):
    username: str
    password: str
    email:EmailStr
    full_name:Union[str,None] = None

class UserOut(BaseModel):
    username: str
    email:EmailStr
    full_name:Union[str,None] = None


class Item(BaseModel):
    name: str
    description: Union[str,None] = None
    price: float
    tax: float = 10.5
    tags:List[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}



app07= APIRouter()
@app07.post("/user02",response_model=UserOut)
def create_user(user:UserIn):
    return user

@app07.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]




