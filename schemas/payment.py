from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PaymentCreate(BaseModel):
    id: int
 
class PaymentResponse(BaseModel):
    id: Optional[int] = None
    user_id: Optional[int] = None
    payment_date: Optional[datetime] = None
