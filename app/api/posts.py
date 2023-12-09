from fastapi import APIRouter , HTTPException , status
from config.database import db_dependency
from typing import List
from app.models import Post
from app.schemas import AddPost , GetPost

router = APIRouter()

@router.get("/post", response_model=List[GetPost])
def read_post(db:db_dependency):
    data= db.query(Post).all()
    # print(GetPost)
    return data

@router.post("/post",response_model=List[GetPost])
def create_post(post:AddPost, db:db_dependency):
    data=Post(
                title=post.title,
                description=post.description,
                category_id=post.category_id
              )
    db.add(data)
    db.commit()
    db.refresh(data)
    return [data]


@router.put("/post/{post_id}",response_model=List[GetPost])
def update_post(post:AddPost, post_id:int , db:db_dependency):
    data=db.query(Post).filter(Post.id==post_id).first()
    if data:
        data.title=post.title
        data.description=post.description
        data.category_id=post.category_id
        db.add(data)
        db.commit()
        db.refresh(data)
        return [data]
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="post not found",
    )


@router.delete("/post/{post_id}")
def delete_post(post_id:int , db:db_dependency):
    data=db.query(Post).filter(Post.id==post_id).first()
    if data:
        db.delete(data)
        db.commit()
       
        return {"details":"post deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="post not found",
    )
