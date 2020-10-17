from typing import List, Optional

from pydantic import BaseModel

class RawArticle(BaseModel):
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