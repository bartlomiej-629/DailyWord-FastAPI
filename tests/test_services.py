from app.services import get_word_of_the_day_article, generate_and_cache_article, set_cached_article, get_cached_article

def test_get_word_of_the_day_article():
    article = get_word_of_the_day_article()
    assert isinstance(article.header, str)
    assert len(article.header) > 0
    assert isinstance(article.body, str)
    assert len(article.body) <= 300
    assert len(article.body) > 0

def test_generate_and_cache_article():
    article = generate_and_cache_article()
    assert isinstance(article.header, str)
    assert len(article.header) > 0
    assert isinstance(article.body, str)
    assert len(article.body) <= 300
    assert len(article.body) > 0

def test_cache_article():
    article = generate_and_cache_article()
    set_cached_article(article)
    cached_article = get_cached_article()
    assert cached_article is not None
    assert cached_article.header == article.header
    assert cached_article.body == article.body
