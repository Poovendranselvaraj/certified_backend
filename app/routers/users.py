from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, models,oauth2
from ..database import get_db

router = APIRouter(tags=['Certificates'])

@router.post("/users/{user_id}/certificates/", response_model=schemas.Certificate)
def create_Certificate(user_id: int, certificate: schemas.CertificateCreate, db: Session = Depends(get_db)):
    return crud.create_certificate(db=db, certificate=certificate, user_id=user_id)

# @router.get("/users/{user_id}/certificates/", response_model=List[schemas.Certificate])
# def read_certificates(user_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     return crud.get_certificates(db=db, user_id=user_id, skip=skip, limit=limit)


# @router.get("/users/certificates/start_day/",response_model=schemas.DayStart)
# def start_day(db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
#     return crud.start_day(db=db, employee_id=current_user.id)

