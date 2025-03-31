from sqlalchemy import Column, String, Text, TIMESTAMP
from app.database import Base

class User(Base):
    __tablename__ = "users"

    usrid = Column(String(50), primary_key=True, index=True)
    level = Column(String(20))
    email = Column(String(255), unique=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    school = Column(String(100))
    password_hash = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    autho = Column(String(50), default="read")
