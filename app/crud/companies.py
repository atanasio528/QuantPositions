from sqlalchemy.orm import Session
from app.models.companies import Company
from app.schemas.companies import CompanyCreate, CompanyUpdate

def get_all_companies(db: Session):
    return db.query(Company).all()

def get_company(db: Session, cpid: str):
    return db.query(Company).filter(Company.cpid == cpid).first()

def create_company(db: Session, company: CompanyCreate):
    db_company = Company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

def update_company(db: Session, cpid: str, updates: CompanyUpdate):
    db_company = get_company(db, cpid)
    if db_company:
        for field, value in updates.dict(exclude_unset=True).items():
            setattr(db_company, field, value)
        db.commit()
        db.refresh(db_company)
    return db_company
