from fastapi import FastAPI, Request, Response
app = FastAPI()
@app.get("/")
def index():
    return {"message": "Hello World"}

