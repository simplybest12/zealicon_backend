from fastapi import FastAPI,APIRouter,HTTPException,status,Depends,Response
from typing import Annotated
import models
from database import database
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from schemas import users
import oauth2
from core.utils import hash
from sqlalchemy.orm import Session

router = APIRouter(
    # prefix="/auth",
    tags=['Auth']
)

get_db = database.get_db
db_dependency = Annotated[Session,Depends(get_db)]

@router.post('/login')

async def login(user_credential:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):

    user = db.query(models.User).filter(models.User.email==user_credential.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    
    if not hash.Hash.verify(user_credential.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    if user.is_admin:
        permissions = "admin"
    else:
        permissions = "user"
    
    access_token = oauth2.create_access_token(
        data={
            "user_id":user.id,
            "user_email":user.email,
            "permissions":permissions
        }
    )
    
    return {"access_token":access_token,
            "token_type":"bearer"
            }
    
    
    

@router.post('/signup', response_model=users.UserResponse, status_code=status.HTTP_201_CREATED,response_model_exclude_none=True)

async def signup(user_instance: users.UserSignUp, db: Session = Depends(get_db)):

    existing_user = db.query(models.User).filter(models.User.email == user_instance.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with this email already exists")
    

    hashed_password = hash.Hash.bcrypt(user_instance.password)
    user_instance.password = hashed_password

    new_user = models.User(
        email=user_instance.email,
        password=user_instance.password,
        username=user_instance.username,
        phone_number=user_instance.phone_number,

    )
    

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user