from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app import crud
from app.schemas.companies import CompanyOut, CompanyCreate, CompanyUpdate

router = APIRouter(prefix="/companies", tags=["Companies"])

@router.get("/", response_model=List[CompanyOut])
def read_companies(db: Session = Depends(get_db)):
    return crud.companies.get_all_companies(db)

@router.get("/{cpid}", response_model=CompanyOut)
def read_company(cpid: str, db: Session = Depends(get_db)):
    db_company = crud.companies.get_company(db, cpid)
    if not db_company:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company

@router.post("/", response_model=CompanyOut)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    return crud.companies.create_company(db, company)

@router.patch("/{cpid}", response_model=CompanyOut)
def update_company(cpid: str, updates: CompanyUpdate, db: Session = Depends(get_db)):
    db_company = crud.companies.update_company(db, cpid, updates)
    if not db_company:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company
