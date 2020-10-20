from typing import List

from fastapi import Depends, APIRouter, HTTPException

from sqlalchemy.orm import Session

from .. import articles_crud, stats_crud, schemas
from ..database import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()


@router.post("/scraper_stats/", response_model=schemas.ScrapingStats)
async def create_stats(stats: schemas.ScrapingStats, db: Session = Depends(get_db)):
    return stats_crud.create_stats(db=db, stats=stats)

@router.get("/scraper_stats/", response_model=List[schemas.ScrapingStats])
async def read_stats(db: Session = Depends(get_db)):
    return stats_crud.get_stats(db=db)