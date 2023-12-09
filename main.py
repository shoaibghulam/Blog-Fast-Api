from fastapi import FastAPI
from app.api import posts , categories , learning
from app.models import Base
from config.database import engine

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(learning.router)
app.include_router(posts.router)
app.include_router(categories.router)