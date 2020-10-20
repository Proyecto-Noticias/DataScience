from sqlalchemy.orm import Session

from . import models, schemas


def create_stats(db: Session, stats: schemas.ScrapingStats):
    db_stats = models.ScrapingStats(response_count=stats.response_count,
    start_time=stats.start_time,
    finish_time=stats.finish_time,
    memory_usage_max=stats.memory_usage_max,
    total_articles_added=stats.total_articles_added,
    scraping_date=stats.scraping_date)

    db.add(db_stats)
    db.commit()
    db.refresh(db_stats)
    return db_stats