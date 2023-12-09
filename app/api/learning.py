from fastapi import APIRouter , HTTPException , status
from config.database import db_dependency
from typing import List
from app.models import Post
from app.schemas import AddPost , GetPost
from pydantic import BaseModel , Field
router = APIRouter()
class BookSchema(BaseModel):
    id:int = Field(gt=0)
    title:str = Field(max_length=300)
    author:str = Field(max_length=300)
    rating:int = Field(gt=-1 , le=11)
    class Config:
        json_schema_extra={
            "title":"New Book Title",
            "author":"New Book Author",
            "rating":2
        }
    
class Book:
    id:int
    title:str
    author:str
    rating:int
    def __init__(self, id, title, author, rating):
        self.id = id
        self.title = title
        self.author = author
        self.rating = rating
        
BOOKS=[
    Book(1,"Learning HTML","Shoaib Ghulam",4),
    Book(1,"Learning HTML","Shoaib ",2),
]
@router.get('/learing')
def get_learing():
    return BOOKS

@router.post('/learing')
def add_learing(content:BookSchema):
    # BOOKS.append(content)
    BOOKS.append(Book(**content.dict()))
    return BOOKS

