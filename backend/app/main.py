from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlalchemy import text
from app.database import engine, Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    # app startup
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        print("Database connection verified.")
    yield
    # app shutdown

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"status":"ok"}