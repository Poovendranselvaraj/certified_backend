from datetime import datetime
from sqlalchemy.orm import Session
from . import models, schemas, utils

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_users(db: Session, user: schemas.UserCreate):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_certificate(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Certificate).filter(models.Certificate.user_id == user_id).offset(skip).limit(limit).all()

# def start_day(db: Session, user_id: int):
#     certificate=models.certificate(user_id=user_id, start_day=datetime.utcnow())
#     db.add(certificate)
#     db.commit()
#     db.refresh(certificate)
#     return certificate


# def create_leave(db: Session, leave: schemas.LeaveCreate, user_id: int):
#     db_leave = models.Leave(
#         user_id=user_id,
#         start_date=leave.start_date,
#         end_date=leave.end_date,
#         reason=leave.reason,
#         approved=False
#     )
#     db.add(db_leave)
#     db.commit()
#     db.refresh(db_leave)
#     return db_leave

# def get_user_leaves(db: Session, user_id: int):
#     return db.query(models.Leave).filter(models.Leave.user_id == user_id).all()

# def approve_leave(db: Session, leave_id: int):
#     db_leave = db.query(models.Leave).filter(models.Leave.id == leave_id).first()
#     if db_leave:
#         db_leave.approved = True
#         db.commit()
#         db.refresh(db_leave)
#     return db_leave
