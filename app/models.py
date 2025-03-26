from pydantic import BaseModel

class Article(BaseModel):
    header: str
    body: str
