from fastapi import FastAPI
from app.services import get_word_of_the_day_article, generate_and_cache_article
from app.scheduler import start as start_scheduler
from app.models import Article

app = FastAPI()

@app.on_event("startup")
def startup_event():
    # Start the scheduler
    start_scheduler()
    # Generate and cache the article on startup
    generate_and_cache_article()

@app.get("/word-of-the-day", response_model=Article)
def read_word_of_the_day():
    article = get_word_of_the_day_article()
    return article
