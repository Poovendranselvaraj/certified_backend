from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models
from .database import engine
from .routers import users, certificates, auth

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
#     return crud.create_user(db=db, user=user)

# @app.post("/users/{user_id}/certificates/", response_model=schemas.Certificate)
# def create_certificate_for_user(
#     user_id: int, certificate: schemas.CertificateCreate, db: Session = Depends(database.get_db)
# ):
#     user = crud.get_user(db=db, user_id=user_id)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return crud.create_certificate(db=db, certificate=certificate, user_id=user_id)


@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(users.router)
app.include_router(certificates.router)
app.include_router(auth.router)
