from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PositionBase(BaseModel):
    pztname: str
    pztlevel: Optional[str] = None  # Intern, NewGrad, ...
    year: int
    url: Optional[str] = None
    jd: Optional[str] = None
    note: Optional[str] = None
    recent: Optional[bool] = False
    active: Optional[bool] = True
    updated_by: Optional[str] = None
    oa_first: Optional[bool] = False

class PositionCreate(PositionBase):
    pztid: str
    cpid: str

class PositionUpdate(PositionBase):
    pass

class PositionOut(PositionBase):
    pztid: str
    cpid: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
