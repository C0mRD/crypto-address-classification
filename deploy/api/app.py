from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from logger import logger
import uvicorn
from routers import inference

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logger.info("Starting application")
        yield
    finally:
        logger.info("Stopping application")

app = FastAPI(title="Crypto Classification", version="1.0.0", lifespan=lifespan)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET','POST','PUT','DELETE'],
    allow_headers=["*"],
)

app.include_router(inference.router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)