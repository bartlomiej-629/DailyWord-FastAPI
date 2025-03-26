import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    WORDSMITH_RSS_FEED = os.getenv('WORDSMITH_RSS_FEED')
    CACHE_TTL = int(os.getenv('CACHE_TTL', 86400))