# app/routers/auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.users import UserLogin, Token, UserOut
from app.crud import users
from app.core.security import verify_password, create_access_token
from app.database import get_db
from app.core.deps import get_current_user
from app.models.users import User

router = APIRouter()

@router.post("/login", response_model=Token)
def login(user_in: UserLogin, db: Session = Depends(get_db)):
    db_user = users.get_user_by_email(db, user_in.email)
    if not db_user or not verify_password(user_in.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token(data={"usrid": db_user.usrid})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=UserOut)
def read_me(current_user: User = Depends(get_current_user)):
    return current_user
