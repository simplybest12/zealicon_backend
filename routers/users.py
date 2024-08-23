from fastapi import FastAPI,APIRouter,HTTPException,status,Depends,Response
import models
from database import database
from schemas import users
from sqlalchemy.orm import Session
from core.utils import hash
from oauth2 import get_current_admin_user,get_current_user
from typing import Annotated,List

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

get_db = database.get_db
db_dependency = Annotated[Session,Depends(get_db)]

@router.post('/',response_model=users.UserResponse,status_code=status.HTTP_201_CREATED,response_model_exclude_none=True)

async def user_create(user_instance:users.UserCreate,db:db_dependency,current_user = Depends(get_current_admin_user)):
    user = db.query(models.User).filter(models.User.email == user_instance.email).first()
 
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="User with this email already exists")
    
    hashed_password = hash.Hash.bcrypt(user_instance.password)
    user_instance.password=hashed_password
    db_user = models.User(
        **user_instance.dict()
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get('/users',response_model=list[users.UserResponse],status_code=status.HTTP_200_OK,)

async def fetch_users(db:db_dependency,current_user = Depends(get_current_admin_user)):
    users = db.query(models.User).limit(15).all()
    return users

@router.get('/user/{uid}',response_model=users.UserResponse,response_model_exclude_none=True,status_code=status.HTTP_200_OK)

async def fetch_user(uid:int,db:db_dependency,current_user = Depends(get_current_user)):
    user = db.query(models.User).filter(models.User.id==uid).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {uid} not found")
    
    if current_user.id != uid and not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Not authorized to perform requested action")
    return user


@router.delete(
    "/delete_user/{uid}",
    status_code=status.HTTP_204_NO_CONTENT,
    
)

async def delete_user(uid:int,db:db_dependency,current_user = Depends(get_current_admin_user)):
    db_user = db.query(models.User).filter(models.User.id == uid)
    if not db_user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    db_user.delete(synchronize_session=False)
    db.commit()
    return {"message":"user deleted"}


@router.get('/me', response_model=users.UserResponse)
async def read_users_me(current_user: models.User = Depends(get_current_user)):
    return current_user