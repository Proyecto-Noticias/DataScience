from enum import unique
from sqlalchemy import Column, Integer, String, Text

from .database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(300), nullable=False)
    subtitle = Column(String(300), nullable=False)
    article_date = Column(String(50), nullable=False)
    image_url = Column(String(200), nullable=True)
    category_id = Column(Integer)
    body = Column(Text, nullable=False)
    article_url = Column(String(200), unique=True, nullable=False)
    journal_id = Column(Integer)
    scraping_date = Column(String(50), nullable=False)
    


