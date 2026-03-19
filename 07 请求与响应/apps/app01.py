from fastapi import APIRouter

app01= APIRouter()

@app01.get("/user/1")
def get_user():
    print("id",id)
    return {"user_id":id}


@app01.get("/user/{id}")
def get_user(id):
    print("id",id)
    return {"user_id":id}


@app01.get("/article/{id}")
def get_article(id):
    print("id",id)
    return {"article_id":id}

