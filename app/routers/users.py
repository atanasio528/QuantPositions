from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.users import UserCreate, UserOut
from app import crud

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # existing = crud.users.get_user_by_email(db, user.email)
    # if existing:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    # return crud.users.create_user(db, user)
    raise ValueError("Manually inserted user list, don't implement create function")
    return None


@router.get("/", response_model=List[UserOut])
def list_users(db: Session = Depends(get_db)):
    # return crud.users.get_all_users(db)
    raise ValueError("Manually inserted user list, don't implement create function")
    return None

@router.get("/{usrid}", response_model=UserOut)
def read_user(usrid: str, db: Session = Depends(get_db)):
    user = crud.users.get_user_by_id(db, usrid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
