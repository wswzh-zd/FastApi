from fastapi import APIRouter
from pydantic import BaseModel
from datetime import date
from typing import List

app03= APIRouter()

class User(BaseModel):
    name : str
    age : int
    birth : date
    friends : List[int]



@app03.post("/user")
def user(user:User):
    print("user :",type(user))
    return {
    }

@app03.post("/data")
def data():

    return data








