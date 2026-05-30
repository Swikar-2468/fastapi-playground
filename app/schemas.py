from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email : EmailStr
    password : str    

class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime

class UserLogin(BaseModel):
    email:EmailStr
    password : str


class PostBase(BaseModel):
    title:str
    content:str
    published:bool = True

class PostCreate(PostBase): #inherit postbase attributes
    pass #instead of asking the user for their user id when they are creating a post, what we need to do is that the user id should be taken automatically from the token

#class for response: this is the response model based on how the response will be generated for the user
class Post(PostBase):
    id:int
    created_at:datetime
    owner_id:int
    owner : UserOut

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id : Optional[int] = None