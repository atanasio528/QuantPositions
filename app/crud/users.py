from sqlalchemy.orm import Session
from app.models.users import User
from app.schemas.users import UserCreate
from datetime import datetime
import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def get_user_by_id(db: Session, usrid: str):
    return db.query(User).filter(User.usrid == usrid).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_all_users(db: Session):
    return db.query(User).all()

def create_user(db: Session, user: UserCreate):
    db_user = User(
        usrid=user.usrid,
        level=user.level,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        school=user.school,
        password_hash=hash_password(user.password),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        autho=user.autho,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
