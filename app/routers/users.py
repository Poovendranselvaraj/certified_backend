from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas, models,oauth2
from ..database import get_db

router = APIRouter()



@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return db_user

@router.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users
