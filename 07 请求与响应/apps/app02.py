from fastapi import APIRouter

app02= APIRouter()

@app02.get("/jobs/{kd}")
def get_jobs(kd,xl=None,gj=None):

    return {
        "kd":kd,
        "xl":xl,
        "gj":gj,
    }