from fastapi import FastAPI
from app.routers import example
from config.settings import get_settings
import logging
from contextlib import asynccontextmanager

logger = logging.getLogger("uvicorn")

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application startup")
    settings = get_settings()
    logger.info(f"Loaded settings: {settings}")
    yield
    logger.info("Application shutdown")

app = FastAPI(title="Enterprise FastAPI Template", lifespan=lifespan)

# Include routers
app.include_router(example.router)
