from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_word_of_the_day():
    response = client.get("/word-of-the-day")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data['header'], str)
    assert len(data['header']) > 0
    assert isinstance(data['body'], str)
    assert len(data['body']) <= 300
    assert len(data['body']) > 0
    assert "usage" in data['body'] or "definition" in data['body']
