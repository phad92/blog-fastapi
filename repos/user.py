import sys
sys.path.append("..")

from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session
from hashing import Hash
import models, schemas


def create(request: schemas.User, db: Session ):
    user = models.User(name=request.name, email=request.email, password = Hash.bcrypt(request.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return request


def show(id:int, db: Session):
    userModel = models.User
    user = db.query(userModel).filter(userModel.id == id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found")
    
    return user

def get_all(db):
    users = db.query(models.Blog).all()
   
    if not users:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"users not found")
   
    return users
