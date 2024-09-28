from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models
from .database import engine
from .routers import users, auth

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

app.include_router(users.router)
# app.include_router(certificates.router)
app.include_router(auth.router)
