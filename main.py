from fastapi import FastAPI,APIRouter
from core.config import settings
from database.database import engine,Base
from routers import users,auth,payment
from sqlalchemy import inspect


def create_table():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.project_name,version=settings.project_version)
    create_table()
    return app

app = start_application()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(payment.router)