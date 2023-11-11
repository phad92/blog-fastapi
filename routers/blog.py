import sys
sys.path.append("..")

from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List
import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter()

@router.post('/blog', status_code=status.HTTP_201_CREATED, response_model=List[schemas.ShowBlog], tags=["blog"])
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog

@router.get('/blogs', tags=['blog'])
# def all(db:Session = Depends(database.get_db),limit=10, published: bool = True, sort: Optional[str] = None):
def all(db:Session = Depends(database.get_db)):
   blogs = db.query(models.Blog).all()
   return blogs
    
@router.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog, tags=["blog"])
def show(id:int, response: Response, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
      
    return blog

@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["blog"])
def destroy(id:int, db: Session=Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return { "status": True }

@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=["blog"])
def update(id, request: schemas.Blog, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")
    blog.update(request.model_dump())
    db.commit()
    return 'updated'  