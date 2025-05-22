from fastapi import FastAPI
from contextlib import asynccontextmanager
# from app.db import connect_to_mongo
from app.routes import exercises

@asynccontextmanager
async def lifespan(app: FastAPI):
    # await connect_to_mongo()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(exercises.router, prefix="/exercises", tags=["exercises"])

@app.get("/")
async def root():
    return {"message": "Gym Tracker!"}

