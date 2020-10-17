from sqlalchemy.orm import Session

from . import models, schemas


def create_raw_article(db: Session, raw_article: schemas.RawArticle):
    db_raw_article = models.RawArticle(title = raw_article.title,
     subtitle = raw_article.subtitle,
     article_date = raw_article.article_date,
     image_url = raw_article.image_url,
     category_id = raw_article.category_id,
     body = raw_article.body,
     article_url = raw_article.article_url,
     journal_id = raw_article.journal_id,
     scraping_date = raw_article.scraping_date
     )
    db.add(db_raw_article)
    db.commit()
    db.refresh(db_raw_article)
    return db_raw_article

