import sys
sys.path.append("..")

from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List
import schemas, models
from database import get_db
from hashing import Hash
from sqlalchemy.orm import Session
from repos import user

router = APIRouter(
    prefix="/user",
    tags=['users']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    # user = models.User(name=request.name, email=request.email, password = Hash.bcrypt(request.password))
    # db.add(user)
    # db.commit()
    # db.refresh(user)
    # return request
    return user.create(request, db)


@router.get('/all')
# def all(db:Session = Depends(get_db),limit=10, published: bool = True, sort: Optional[str] = None):
def get_users(db:Session = Depends(get_db)):
#    users = db.query(models.Blog).all()
   
#    if not users:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"users not found")
   
#    return users
    return user.get_all(db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(get_db)):
    # userModel = models.User
    # user = db.query(userModel).filter(userModel.id == id).first()
    
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found")
    
    # return user
    return user.show(id, db)
    