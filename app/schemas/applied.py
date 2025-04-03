from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AppliedBase(BaseModel):
    applied: Optional[bool] = False
    applied_at: Optional[datetime] = None

class AppliedCreate(AppliedBase):
    usrid: str
    pztid: str
    cpid: str

class AppliedUpdate(AppliedBase):
    pass

class AppliedOut(AppliedBase):
    usrid: str
    pztid: str

    class Config:
        orm_mode = True