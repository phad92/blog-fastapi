import sys
sys.path.append("..")

from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List
from sqlalchemy.orm import Session
import schemas, database, models, oauth2
from repos import blog



router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog
    # return blog.create(request, db)

@router.get('/all')
# def all(db:Session = Depends(database.get_db),limit=10, published: bool = True, sort: Optional[str] = None):
def all(db:Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
   return blog.get_all(db)
    
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id:int, db: Session = Depends(database.get_db)):
   return blog.show(id, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session=Depends(database.get_db)):
   return blog.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update(id, request, db)
