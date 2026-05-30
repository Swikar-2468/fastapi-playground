from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from .. import oauth2, schemas, models, utils


router = APIRouter(tags = ['Authentication'])

@router.post('/login')
def login(user_credentials:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first() #OAuth2PasswordRequestForm has only 2fields called username and password, for our usecase, the username houses the email. for this we cannot enter data in json but in form data.
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = 'Invalid Credentials')
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = 'Invalid Credentials')
    
    access_token = oauth2.create_access_token(data = {"user_id" : user.id})


    return {"access token" : access_token, "token_type": "bearer"}
