from fastapi import FastAPI
import uvicorn
from fastapi.templating import   Jinja2Templates
from tortoise.contrib.fastapi import register_tortoise
from settings import TORTOISE_ORM

app = FastAPI()

register_tortoise(
    app=app,
    config=TORTOISE_ORM,
)



templates = Jinja2Templates(directory="templates")

if __name__ == "__main__":
    uvicorn.run("main:app",host='127.0.0.1',port=8010,
                reload=True,workers=1)





















