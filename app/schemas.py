from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class CertificateBase(BaseModel):
    # date: datetime
    # status: str
    pass

class CertificateCreate(CertificateBase):
    pass


class TokenData(BaseModel):
    id: Optional[str] = None



class Certificate(CertificateBase):
    id: int
    user_id: int
    start_day: datetime
    end_day: Optional[datetime]

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str
    

class UserCreate(UserBase):
    password: str
    
    class Config:
        # this is required to avoid errors when serializing, deserializing
        orm_mode = True



class User(UserBase):
    id: int
    certificate: List[Certificate] = []

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token:str
    Token_type: str

class LoginRequest(BaseModel):
    email: str
    password: str


class BreakStart(BaseModel):
    start_break: datetime
    reason: str

class BreakEnd(BaseModel):
    end_break: datetime
    

class DayStart(BaseModel):
    start_day: datetime

class DayEnd(BaseModel):
    end_day: datetime
    work_done: str


class LeaveCreate(BaseModel):
    start_date: datetime
    end_date: datetime
    reason: str

class LeaveResponse(BaseModel):
    id: int
    User_id: int
    start_date: datetime
    end_date: datetime
    reason: str
    approved: bool

    class Config:
        orm_mode = True
