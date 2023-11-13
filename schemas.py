from pydantic import BaseModel
from typing import List
   
class BlogBase(BaseModel):
    title: str
    body: str
    
class Blog(BlogBase):
    class Config():
        orm_mode = True
   
    # user_id: int
    
    
# show specific items form a model 
class ShowBlog(BaseModel):
    title: str
    body: str
    # creator: ShowUser
    class Config():
        orm_mode = True
        
class User(BaseModel):
    name: str
    email: str
    password: str
    
class ShowUser(BaseModel):
    email: str
    name: str
    blogs: List[Blog]
    class Config():
        orm_mode = True
        

class Login(BaseModel):
    username: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
