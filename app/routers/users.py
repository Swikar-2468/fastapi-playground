from fastapi import FastAPI, status, HTTPException, Depends, APIRouter
from typing import Optional, List
from random import randrange
import psycopg2 
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from app.database import engine, get_db, Base

#stating the default hashing algorihtms
# models.Base.metadata.create_all(bind = engine)

router = APIRouter(
    prefix = '/users',
    tags=['Users']

)

@router.post("/", status_code = status.HTTP_201_CREATED, response_model = schemas.UserOut)
def create_user(user:schemas.UserCreate, db:Session = Depends(get_db)): 

    # hash the passowrd
    hashed_pwd = utils.hash(user.password)
    user.password = hashed_pwd

    new_user = models.User(**user.dict()) #unpacks the schema dynamically
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id:int, db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'User with id : {id} was not found')
    return user