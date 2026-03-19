from fastapi import APIRouter, UploadFile
from pydantic import BaseModel
from datetime import date
from typing import List

from fastapi import Request

app06= APIRouter()
@app06.post("/items")
def get_file(request:Request):
    print("URL",request.url)
    print("客户端IP地址",request.client.host)
    return {
    }





