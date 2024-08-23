from pydantic import BaseModel
import typing as t
from datetime import datetime
from .payment import PaymentResponse 

class UserBase(BaseModel):
    username: str
    email: str
    is_admin: bool=False
    phone_number: str
    created_at: datetime
    ispaymentdone: bool
    
class UserSignUp(BaseModel): 
    username: str
    email: str
    phone_number: str
    password:str
    


class UserCreate(UserBase):
    password:str
    class Config:
        from_attributes = True

class UserResponse(UserBase):
    id:int
    payment: t.Optional[PaymentResponse] = None
    
    class Config:
        from_attributes = True

    
    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id:int
    email: t.Optional[str] = None
    permissions: str = "user"