from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from app import models, api_models, utils
from app.database import get_db


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=api_models.UserOut)
def create_user(user: api_models.UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@router.get('/{id}', response_model=api_models.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user_details = db.query(models.User).filter(models.User.id == id).first()
    if not user_details:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post with id: {id} does not exist")
    return user_details