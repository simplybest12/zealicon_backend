from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import random
from database.database import Base


class User(Base):
    __tablename__ = "users" 
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    ispaymentdone = Column(Boolean, default=False)
    
    created_at = Column(DateTime, default=datetime.now)
    
    #database me reflect krana h to foreign key ka use kr skte ho

    # Define a one-to-one relationship with Payment
    payment = relationship("Payment",  uselist=False, back_populates="user")

class Payment(Base):
    __tablename__ = "payments"
    
    id = Column(Integer, primary_key=True, index=True)
    payment_date = Column(DateTime, default=datetime.now)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User",foreign_keys=[user_id], back_populates="payment")
