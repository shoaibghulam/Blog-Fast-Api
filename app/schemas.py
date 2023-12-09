from pydantic import BaseModel , Field 
from typing import Optional
from datetime import datetime
class AddCategory(BaseModel):
    title: str

class GetCategory(BaseModel):
    id:int
    title: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
class AddPost(BaseModel):
    title: str
    description: str
    category_id: int  

class GetPost(BaseModel):
    id:int
    title: str
    description: str
    category_id: int  
    category: Optional[GetCategory] = ["shaoib"]

   
    class Config:
        orm_mode = True
       