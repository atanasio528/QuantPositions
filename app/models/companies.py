from sqlalchemy import Column, String, Integer, TIMESTAMP
from app.database import Base

class Company(Base):
    __tablename__ = "companies"

    cpid = Column(String(50), primary_key=True)
    cpname = Column(String(255), nullable=False)
    industry = Column(String(50))
    importance = Column(Integer, default=99)
    headquarter = Column(String(100))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    updated_by = Column(String(100))
