# app/services.py
import requests
from xml.etree import ElementTree
import openai
from cachetools import TTLCache
from app.config import Config
from app.models import Article

# Create a TTL cache that expires after the specified TTL
cache = TTLCache(maxsize=1, ttl=Config.CACHE_TTL)

def fetch_word_of_the_day(rss_feed_url):
    response = requests.get(rss_feed_url)
    root = ElementTree.fromstring(response.content)
    item = root.find('./channel/item')
    title = item.find('title').text
    description = item.find('description').text
    return title, description

def generate_article(word, description, openai_api_key):
    openai.api_key = openai_api_key
    prompt = (
        "The word of the day is '{}'. Create an article with:\n"
        "1. A header between 40-60 characters.\n"
        "2. A body up to 300 characters explaining the word '{}', including its meaning, usage, and interesting facts.\n\n"
        "Ensure the body is concise, informative, and does not exceed 300 characters. Do not include labels like 'Header' or 'Body'. Use simple and easy english a lot."
    ).format(word, word)


    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    content = response['choices'][0]['message']['content'].strip().split('\n')
    header = content[0]
    body = ' '.join(content[1:])[:300]
    return header, body

def get_cached_article():
    try:
        return cache['article']
    except KeyError:
        return None

def set_cached_article(article):
    cache['article'] = article

def generate_and_cache_article():
    word, description = fetch_word_of_the_day(Config.WORDSMITH_RSS_FEED)
    header, body = generate_article(word, description, Config.OPENAI_API_KEY)
    article = Article(header=header, body=body)
    set_cached_article(article)
    return article

def get_word_of_the_day_article():
    cached_article = get_cached_article()
    if cached_article:
        return cached_article
    return generate_and_cache_article()
