from fastapi import FastAPI

app = FastAPI()


@app.get('/public')
def public():
    return "uvicorn public endpoint"


@app.get('/private')
def private():
    return "uvicorn private endpoint"
