from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.applied import AppliedCreate, AppliedOut, AppliedUpdate
from app import crud

router = APIRouter(prefix="/applied", tags=["Applied"])

@router.get("/", response_model=List[AppliedOut])
def list_applied(db: Session = Depends(get_db)):
    return crud.applied.get_all_applied(db)

@router.get("/user/{usrid}", response_model=List[AppliedOut])
def get_user_applied(usrid: str, db: Session = Depends(get_db)):
    return crud.applied.get_user_applied(db, usrid)

@router.post("/", response_model=AppliedOut)
def create_applied(data: AppliedCreate, db: Session = Depends(get_db)):
    return crud.applied.create_applied(db, data)

@router.put("/{usrid}/{pztid}", response_model=AppliedOut)
def update_applied(usrid: str, pztid: str, updates: AppliedUpdate, db: Session = Depends(get_db)):
    updated = crud.applied.update_applied(db, usrid, pztid, updates)
    if not updated:
        raise HTTPException(status_code=404, detail="Applied record not found")
    return updated
