from sqlalchemy import Column,String,Integer,Text,ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base
from config.mixins import Timestamp
class Category(Timestamp,Base):
    __tablename__="category"
    id=Column(Integer,primary_key=True , index=True)
    title=Column(String(150))
    rel_post=relationship("Post",back_populates='rel_category')
    
class Post(Timestamp,Base):
    __tablename__="post"
    id=Column(Integer,primary_key=True, index=True)
    title=Column(String(150), nullable=False)
    description=Column(Text , nullable=False)
    category_id=Column(Integer, ForeignKey('category.id'))
    rel_category=relationship('Category', back_populates='rel_post')
    