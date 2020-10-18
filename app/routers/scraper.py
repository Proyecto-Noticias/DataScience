from fastapi import Depends, APIRouter, HTTPException

from sqlalchemy.orm import Session

from .. import articles_crud, schemas
from ..database import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.post("/articles/", response_model=schemas.Article)
async def create_article(article: schemas.Article, db: Session = Depends(get_db)):
    db_article = articles_crud.get_article_by_url(db, article_url=article.article_url)
    if db_article:
        raise HTTPException(status_code=400, detail="Article already registered")
    return articles_crud.create_article(db=db, article=article)