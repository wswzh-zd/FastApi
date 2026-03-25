from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn


from fastapi.templating import   Jinja2Templates
from fastapi import Request
app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get("/index")
def index(request:Request):
    name = "root"
    books = [
        "斗罗大陆",
        "斗破苍穹",
        "天行",


    ]

    info = {"name":"rain","age":32,"gender":"male"}
    return templates.TemplateResponse(
        "index.html",
        {
            "request":request,
            "user":name,
            "age":32,
            "books":books,
            "info":info
        }
    )


if __name__ == "__main__":
    uvicorn.run("main:app",port=8080,reload=True)












