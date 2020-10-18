from typing import Optional

from pydantic import BaseModel

class Article(BaseModel):
    id: int
    title: str 
    subtitle: str
    article_date: str
    image_url: Optional[str] = None
    category_id: int
    body: str
    article_url: str 
    journal_id: int
    scraping_date: Optional[str] = None

    class Config:
        orm_mode = True

class ScrapingStats(BaseModel):
    id: int
    response_count: int
    start_time: str
    finish_time: str
    memory_usage_max: int
    total_articles_added: int
    scraping_date: str

    class Config:
        orm_mode = True