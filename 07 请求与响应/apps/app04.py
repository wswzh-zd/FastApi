from fastapi import APIRouter
from pydantic import BaseModel
from datetime import date
from typing import List

from fastapi import Form
app04= APIRouter()
@app04.post("/regin")
def user(username:str=Form(),password:str=Form()):
    print(f"username:{username},password:{password}")
    return {"username":username
    }








