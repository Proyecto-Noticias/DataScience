from fastapi import Depends, APIRouter, HTTPException

from sqlalchemy.orm import Session

from .. import raw_articles_crud, schemas
from ..database import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.post("/raw_articles/", response_model=schemas.RawArticle)
async def create_raw_articles(raw_article: schemas.RawArticle, db: Session = Depends(get_db)):
    db_article = raw_articles_crud.get_article_by_url(db, article_url=raw_article.article_url)
    if db_article:
        raise HTTPException(status_code=400, detail="Article already registered")
    return raw_articles_crud.create_raw_article(db=db, raw_article=raw_article)