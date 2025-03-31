from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.positions import PositionCreate, PositionOut, PositionUpdate
from app import crud

router = APIRouter(prefix="/positions", tags=["Positions"])

@router.get("/", response_model=List[PositionOut])
def list_positions(db: Session = Depends(get_db)):
    return crud.positions.get_all_positions(db)

@router.get("/{pztid}", response_model=PositionOut)
def get_position(pztid: str, db: Session = Depends(get_db)):
    position = crud.positions.get_position_by_id(db, pztid)
    if not position:
        raise HTTPException(status_code=404, detail="Position not found")
    return position

@router.post("/", response_model=PositionOut)
def create_position(position: PositionCreate, db: Session = Depends(get_db)):
    return crud.positions.create_position(db, position)

@router.put("/{pztid}", response_model=PositionOut)
def update_position(pztid: str, updates: PositionUpdate, db: Session = Depends(get_db)):
    updated = crud.positions.update_position(db, pztid, updates)
    if not updated:
        raise HTTPException(status_code=404, detail="Position not found")
    return updated
