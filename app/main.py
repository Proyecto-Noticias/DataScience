from fastapi import Depends, FastAPI, Header, HTTPException

from .routers import scraper

app = FastAPI()


app.include_router(
    scraper.router,
    prefix="/api/v1/scraper",
    tags=["scraper"],
    responses={404: {"description": "Not found"}},
)