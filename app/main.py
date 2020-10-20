from app.models import Category
from typing import List

from fastapi import Depends, FastAPI

from . import models
from .database import SessionLocal, engine
from .routers import articles, stats, generals

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="EasyNews DataScience API",
    description="REST API which serves new and historical news content scraped from the web.",
    version="1.0",)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(
    articles.router,
    prefix="/api/v1",
    tags=["News Articles Endpoints"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    stats.router,
    prefix="/api/v1",
    tags=["Stats Endpoints"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    generals.router,
    prefix="/api/v1",
    tags=["Generals Endpoints"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)