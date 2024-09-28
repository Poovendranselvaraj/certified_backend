from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models
from .database import engine
from .routers import users, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:5173",  # Your frontend origin
    "http://127.0.0.1:5173",  # Alternative frontend origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows requests from your frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

app.include_router(users.router)
# app.include_router(certificates.router)
app.include_router(auth.router)
