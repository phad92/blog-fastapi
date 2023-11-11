from fastapi import FastAPI
import models
from database import engine 
from routers import blog, user
# from passlib.context import CryptContext

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** is also here"
    },
    {
        "name": "blog",
        "description": "Manage Items",
    },
    # {
    #     "name": "items",
    #     "description": "Manage Items",
    #     "externalDocs": {
    #         "description": "Items external docs",
    #         "url": "https://fastapi.tiangolo.com"
    #     },
    # },
]


app = FastAPI(openapi_tags=tags_metadata)

app.include_router(blog.router)
app.include_router(user.router)


models.Base.metadata.create_all(engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally: 
#         db.close()

# @app.post('/blog', status_code=status.HTTP_201_CREATED, response_model=List[schemas.ShowBlog], tags=["blog"])
# def create(request: schemas.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body, user_id = 1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
    
#     return new_blog

# @app.get('/blogs', tags=['blog'])
# # def all(db:Session = Depends(get_db),limit=10, published: bool = True, sort: Optional[str] = None):
# def all(db:Session = Depends(get_db)):
#    blogs = db.query(models.Blog).all()
#    return blogs
    
# @app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog, tags=["blog"])
# def show(id:int, response: Response, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return { 'detail': f"Blog with the id {id} is not available" }
#     return blog

# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["blog"])
# def destroy(id:int, db: Session=Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return { "status": True }

# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=["blog"])
# def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")
#     blog.update(request.model_dump())
#     db.commit()
#     return 'updated'  

# pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated = "auto")
# @app.post('/user', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser, tags=["users"])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     user = models.User(name=request.name, email=request.email, password = Hash.bcrypt(request.password))
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return request

# @app.get('/user/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser, tags=["users"])
# def get_user(id:int, db: Session = Depends(get_db)):
#     userModel = models.User
#     user = db.query(userModel).filter(userModel.id == id).first()
    
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found")
    
#     return user
    
# @app.get('/users', tags=["users"])
# # def all(db:Session = Depends(get_db),limit=10, published: bool = True, sort: Optional[str] = None):
# def get_users(db:Session = Depends(get_db)):
#    users = db.query(models.Blog).all()
   
#    if not users:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"users not found")
   
#    return users
    
# @app.get('/blog/{id}/comment')
# def comment(id:int, limit: int = 10):
#     return { "data": f'{ limit } comment from blog id {id}' }

# class Blog(BaseModel):
#     title: str
#     body: str
#     published: Optional[bool]

# @app.post('/blog')
# def create_blog(request: Blog):
    
#     return request
#     return { "data": "blog created" }

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/items/{id}")
# async def read_item(id:int):
#     return {"item_id": id}