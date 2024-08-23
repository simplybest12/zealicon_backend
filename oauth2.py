from jose import JWTError , jwt
from datetime import datetime,timedelta
from schemas import users
from core.config import settings
import models
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database.database import get_db
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = 'login')

SECRET_KEY = settings.secret_key 
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes
print(ACCESS_TOKEN_EXPIRE_MINUTES)

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token:str,credential_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        id = payload.get("user_id")
        email = payload.get("user_email")
        permissions = payload.get("permissions")
        if email is None:
            
            raise credential_exception
        token_data = users.TokenData(id=id,email=email,permissions=permissions)
    except JWTError:
        raise credential_exception
    return token_data


def get_current_user(token:str = Depends(oauth2_scheme),db:Session=Depends(get_db)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate credentials",
    headers={"WWW-Authenticate":"Bearer"}
    )
    token_data = verify_access_token(token, credential_exception)
    current_user = db.query(models.User).filter(
        models.User.email == token_data.email
    ).first()
    
    if not current_user:
        raise credential_exception

    return current_user
                                          
        
def get_current_admin_user(current_user:models.User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform requested action")
    return current_user

