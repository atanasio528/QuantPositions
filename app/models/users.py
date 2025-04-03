from sqlalchemy import Column, String, Text, TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"
    usrid = Column(String(10), primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(100), nullable=False)
    address_first = Column(String(100), nullable=True)
    address_second = Column(String(100), nullable=True)
    school = Column(String(100), nullable=True)
    level = Column(String(10))
    password_hash = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
    autho = Column(String(50), default="read")
    cover_letter = Column(Text, nullable=True)

    def __repr__(self):
        return f"<User {self.usrid} ({self.email})>"

class CoverLetter(Base):
    __tablename__ = "users"
    usrid = Column(String(10), primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(100), nullable=False)
    address_first = Column(String(100), nullable=True)
    address_second = Column(String(100), nullable=True)
    cover_letter = Column(Text, nullable=True)