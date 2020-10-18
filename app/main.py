from typing import List

from fastapi import Depends, FastAPI

from . import models
from .database import SessionLocal, engine
from .routers import articles

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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