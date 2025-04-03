from sqlalchemy.orm import Session
from app.models.positions import Position
from app.schemas.positions import PositionCreate, PositionUpdate
from datetime import datetime

def get_all_positions(db: Session):
    return db.query(Position).all()

def get_position_by_id(db: Session, cpid: str, pztid: str):
    return db.query(Position).filter(Position.cpid == cpid, Position.pztid == pztid).first()

def create_position(db: Session, position: PositionCreate):
    db_position = Position(
        pztid=position.pztid,
        cpid=position.cpid,
        pztname=position.pztname,
        pztlevel=position.pztlevel,
        year=position.year,
        url=position.url,
        jd=position.jd,
        note=position.note,
        recent=position.recent,
        active=position.active,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        updated_by=position.updated_by,
        oa_first=position.oa_first,
    )
    db.add(db_position)
    db.commit()
    db.refresh(db_position)
    return db_position

def update_position(db: Session, pztid: str, updates: PositionUpdate):
    db_position = get_position_by_id(db, pztid)
    if db_position:
        for field, value in updates.dict(exclude_unset=True).items():
            setattr(db_position, field, value)
        db_position.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_position)
    return db_position
