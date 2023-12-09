from fastapi import APIRouter , HTTPException , status
from config.database import db_dependency
from typing import List
from app.models import Category
from app.schemas import AddCategory , GetCategory

router = APIRouter()

@router.get("/category", response_model=List[GetCategory])
def read_category(db:db_dependency):
    data= db.query(Category).all()
    return data

@router.post("/category",response_model=List[GetCategory])
def create_category(category:AddCategory, db:db_dependency):
    data=Category(title=category.title)
    db.add(data)
    db.commit()
    db.refresh(data)
    return [data]


@router.put("/category/{cat_id}",response_model=List[GetCategory])
def update_category(category:AddCategory, cat_id:int , db:db_dependency):
    data=db.query(Category).filter(Category.id==cat_id).first()
    if data:
        data.title=category.title
        db.add(data)
        db.commit()
        db.refresh(data)
        return [data]
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Category not found",
    )


@router.delete("/category/{cat_id}")
def delete_category(cat_id:int , db:db_dependency):
    data=db.query(Category).filter(Category.id==cat_id).first()
    if data:
        db.delete(data)
        db.commit()
       
        return {"details":"Category deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Category not found",
    )

