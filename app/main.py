from typing import List

from fastapi import Depends, FastAPI

from . import models
from .database import SessionLocal, engine
from .routers import scraper

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(
    scraper.router,
    prefix="/api/v1/scraper",
    tags=["scraper"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)