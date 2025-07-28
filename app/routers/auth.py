from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import models, api_models, database, utils, oauth2

router = APIRouter(tags=['Authentication'])

@router.post('/login', response_model=api_models.Token)
def login(user_cred: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    user_details = db.query(models.User).filter(
        models.User.email == user_cred.username).first()
    
    if not user_details:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials"
        )
    
    if not utils.verify(user_cred.password, user_details.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Password"
        )
    access_token = oauth2.create_access_token(data = {"user_id": user_details.id})

    return {"access_token": access_token, "token_type": "bearer"}