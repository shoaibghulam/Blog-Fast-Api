from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker , Session
from sqlalchemy.ext.declarative import declarative_base
from fastapi import Depends
from typing import Annotated
DB_URI="sqlite:///./database.db"
engine=create_engine(DB_URI , connect_args={'check_same_thread':False})
localSession=sessionmaker(autocommit=False, autoflush=False , bind=engine)
Base = declarative_base()

def get_db():
    db=localSession()
    try:
        yield db
    finally:
        db.close()
        
db_dependency=Annotated[Session , Depends(get_db)]