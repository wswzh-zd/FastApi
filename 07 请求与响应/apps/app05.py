from fastapi import APIRouter, UploadFile
from pydantic import BaseModel
from datetime import date
from typing import List

from fastapi import File,UploadFile

app05= APIRouter()
@app05.post("/file")
def get_file(files:bytes=File()):
    return {"file":"file"
    }


@app05.post("/files")
def get_files(files:List[bytes]=File()):
    return {"file":"file"
    }

from fastapi import File,UploadFile
@app05.post("/uploadFile")
def get_files(file:UploadFile):
    print("file",file)
    return {"file":file.filename
    }






