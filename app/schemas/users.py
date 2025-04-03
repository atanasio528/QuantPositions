from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime

class User(BaseModel):
    usrid: str
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    school: Optional[str] = None
    level: Optional[int] = None
    autho: Optional[str] = "read"
    cover_letter: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class UserOut(BaseModel):
    usrid: str
    email: EmailStr
    first_name: str
    last_name: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
