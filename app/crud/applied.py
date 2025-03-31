from sqlalchemy.orm import Session
from app.models.applied import Applied
from app.schemas.applied import AppliedCreate, AppliedUpdate
from datetime import datetime

def get_all_applied(db: Session):
    return db.query(Applied).all()

def get_user_applied(db: Session, usrid: str):
    return db.query(Applied).filter(Applied.usrid == usrid).all()

def create_applied(db: Session, data: AppliedCreate):
    db_item = Applied(
        usrid=data.usrid,
        pztid=data.pztid,
        applied=data.applied,
        applied_at=data.applied_at or datetime.now()
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_applied(db: Session, usrid: str, pztid: str, updates: AppliedUpdate):
    db_item = db.query(Applied).filter(Applied.usrid == usrid, Applied.pztid == pztid).first()
    if db_item:
        for field, value in updates.dict(exclude_unset=True).items():
            setattr(db_item, field, value)
        if updates.applied:
            db_item.applied_at = datetime.utcnow()
        db.commit()
        db.refresh(db_item)
    return db_item