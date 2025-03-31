from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CompanyBase(BaseModel):
    cpname: str
    industry: str
    importance: Optional[int] = 99
    headquarter: Optional[str]
    updated_by: Optional[str] = "system"

class CompanyCreate(CompanyBase):
    cpid: str

class CompanyUpdate(CompanyBase):
    pass

class CompanyOut(CompanyBase):
    cpid: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
