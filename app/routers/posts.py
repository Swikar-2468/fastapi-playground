from fastapi import FastAPI, status, HTTPException, Depends, APIRouter
from typing import Optional, List
from random import randrange
import psycopg2 
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from .. import models, schemas, oauth2 #. means same level and .. means one step above present parent package
from app.database import engine, get_db, Base


router = APIRouter(
    prefix = "/posts",
    tags=['Posts']
)



@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
    # to view all posts
    # posts = db.query(models.Post).all()

    # if we want the user to be able to see only their posts then 
    posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db:Session=Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):

    # new_post = models.Post(title = post.title, content = post.content, published = post.published)
    new_post = models.Post(owner_id = current_user.id, **post.dict()) #unpacks the schema dynamically
    print(current_user.id, current_user.email)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/{id}", response_model=schemas.Post)
def get_posts(id:int, db:Session=Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.id == id).first()


    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} was not found!!!")

    return post

@router.delete('/{id}')
def delete_post(id:int, db:Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id) #returns a query, not data
    if post_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} doesnot exist!!!")
    post = post_query.first()

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Post deletion not Authorized")
    
    post_query.delete(synchronize_session = False)
    db.commit()

    return {"message": "Post deleted successfully"}


@router.put('/{id}', response_model=schemas.Post)
def update_post(id:int, posts:schemas.PostCreate, db:Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} doesnot exist!!!")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Post deletion not Authorized")

    post_query.update(posts.dict(), synchronize_session = False)

    db.commit()

    return post_query.first()