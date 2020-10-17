from fastapi import APIRouter

router = APIRouter()

@router.post("/raw_articles/")
async def save_raw_articles():
    return [{"username": "Foo"}, {"username": "Bar"}]