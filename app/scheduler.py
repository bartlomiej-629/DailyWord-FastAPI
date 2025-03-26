from apscheduler.schedulers.background import BackgroundScheduler
from app.services import generate_and_cache_article

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(generate_and_cache_article, 'cron', hour=0, minute=0)
    scheduler.start()
