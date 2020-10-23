from sqlalchemy.orm import Session

from . import models, schemas, mysql_service


def get_articles_text():
    return mysql_service.get_articles_joined()

def get_articles_by_date(date):
    return mysql_service.get_articles_by_date(date)

def get_articles(db: Session):
    return db.query(models.Article).all()

def get_article_by_url(db: Session, article_url:str):
    return db.query(models.Article).filter(models.Article.article_url==article_url).first()


def create_article(db: Session, article: schemas.Article):
    db_article = models.Article(title = article.title,
     subtitle = article.subtitle,
     article_date = article.article_date,
     image_url = article.image_url,
     category_id = article.category_id,
     body = article.body,
     article_url = article.article_url,
     journal_id = article.journal_id,
     scraping_date = article.scraping_date,
     sentiment_classification = article.sentiment_classification,
     score=article.score,
     magnitude=article.magnitude
     )
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

