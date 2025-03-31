from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    school: Optional[str] = None
    level: Optional[str] = "NewGrad"
    autho: Optional[str] = "read"

class UserCreate(UserBase):
    usrid: str
    password: str

class UserOut(UserBase):
    usrid: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
