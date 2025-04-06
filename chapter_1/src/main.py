from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get("/")
def welcome():
    return {"message":"Welcome to FastApi."}
@app.get("/greet/{name}",response_class=HTMLResponse)
def greet(name:str):
    return f"<h1>Hello {name}</h1>"