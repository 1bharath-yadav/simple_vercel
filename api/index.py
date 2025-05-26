from fastapi import FastAPI, requests
app = FastAPI()
@app.get("/")
def index():
    return {"message": "Hello World"}

