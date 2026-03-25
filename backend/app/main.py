from fastapi import FastAPI
from app import database

app = FastAPI()

@app.get("/")
def root():
    return {"status":"ok"}