from pydantic import BaseModel, Field, EmailStr
from datetime import date, datetime, time, timedelta
from typing import Optional

from pydantic.types import conint

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     created_at: datetime = Field(default_factory=datetime.now) 

# class CreatePost(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     created_at: datetime = Field(default_factory=datetime.now)

# class UpdatePost(BaseModel):
#     published: bool

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    created_at: datetime = Field(default_factory=datetime.now)

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    # class Config:
    #     orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class Vote(BaseModel):
    post_id: str
    dir: conint(le=1)

