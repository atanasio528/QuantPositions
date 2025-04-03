from sqlalchemy.orm import Session
from app.models.users import User, CoverLetter
from app.models.positions import Position
from app.models.companies import Company
from sqlalchemy import and_, or_
# from app.schemas.users import UserCreate
from app.core.security import hash_password
from datetime import datetime

def get_user_by_id(db: Session, usrid: str):
    return db.query(User).filter(User.usrid == usrid).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_all_users(db: Session):
    return db.query(User).all()

# Cover letter related codes
# If user click open positions (given user_id), choose company & position
# give the info for generating cover letter
def get_cover_letters_by_usrid_ptzid(db: Session, usrid: str, cp_pzt_pairs: list[dict]):
    conditions = [
        and_(
            Position.cpid == pair['cpid'],
            Position.pztid == pair['pztid']
        )
        for pair in cp_pzt_pairs
    ]

    user = db.query(CoverLetter).filter(CoverLetter.usrid == usrid).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    cp_pzt_results = (
        db.query(
            Company.cpname,
            Position.pztname,
            Company.headquarter_first,
            Company.headquarter_second
        )
        .join(Position, Position.cpid == Company.cpid)
        .filter(or_(*conditions))
        .all()
    )

    if not cp_pzt_results:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    formatted = []
    for cp in cp_pzt_results:
        formatted.append({
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "address_first": user.address_first,
            "address_second": user.address_second,
            "cpname": cp[0],
            "pztname": cp[1],
            "headquarter_first": cp[2],
            "headquarter_second": cp[3],
            "cover_letter": user.cover_letter
        })

    return formatted


# Annotate due to manual insertion of user information
# def create_user(db: Session, user: UserCreate):
#     db_user = User(
#         usrid=user.usrid,
#         level=user.level,
#         email=user.email,
#         first_name=user.first_name,
#         last_name=user.last_name,
#         school=user.school,
#         password_hash=hash_password(user.password),
#         created_at=datetime.utcnow(),
#         updated_at=datetime.utcnow(),
#         autho=user.autho,
#     )
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
