from typing import List

from fastapi import Depends, APIRouter, HTTPException

from sqlalchemy.orm import Session

from .. import generals_crud, schemas
from ..database import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.get("/categories/", response_model=List[schemas.Category])
async def read_categories(db: Session = Depends(get_db)):
    return generals_crud.get_categories(db=db)

@router.get("/journals/", response_model=List[schemas.Journal])
async def read_journals(db: Session = Depends(get_db)):
    return generals_crud.get_journals(db=db)