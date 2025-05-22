from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db import connect_to_mongo

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongo()
    yield

app = FastAPI(lifespan=lifespan)

