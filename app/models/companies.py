from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base

class Company(Base):
    __tablename__ = "companies"
    cpid = Column(String(50), primary_key=True)
    cpname = Column(String(255), nullable=False)
    industry = Column(String(50), nullable=True)
    importance = Column(Integer, default=99, nullable=True)
    headquarter_first = Column(String(100), nullable=True)
    headquarter_second = Column(String(100), nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
    updated_by = Column(String(100))