from fastapi import FastAPI,APIRouter,HTTPException,status,Depends,Response
import models
from database import database
from schemas import users,payment
from sqlalchemy.orm import Session
from core.utils import hash
from oauth2 import get_current_admin_user,get_current_user
from typing import Annotated,List

router = APIRouter(
    prefix="/payment",
    tags=['Payment']
)

get_db = database.get_db
db_dependency = Annotated[Session,Depends(get_db)]


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=payment.PaymentResponse)
async def create_payment(
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    db_user = db.query(models.Payment).filter(models.Payment.user_id==current_user.id).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Payment already exists")
    # The current_user is already authenticated
    payment_user = models.Payment(
        user_id=current_user.id
    )
    db.add(payment_user)
    db.commit()
    db.refresh(payment_user)
    current_user.ispaymentdone = True
    db.add(current_user)
    db.commit()
       
    return payment_user


@router.get('/pays', status_code=status.HTTP_200_OK, response_model=List[payment.PaymentResponse])

async def fetch_payments(db:db_dependency,current_user = Depends(get_current_admin_user)):
    payments = db.query(models.Payment).all()
    return payments

@router.get('/pays/{pid}',status_code=status.HTTP_200_OK,response_model=payment.PaymentResponse)

async def fetch_payment(db:db_dependency,current_user = Depends(get_current_admin_user)):
    payment = db.query(models.Payment).filter(models.Payment.user_id==current_user.id).first()
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Payment not found")
    return payment