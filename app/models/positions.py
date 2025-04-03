from sqlalchemy import Column, String, Integer, Boolean, Text, ForeignKey, TIMESTAMP
from app.database import Base
from sqlalchemy.sql import func

class Position(Base):
    __tablename__ = "positions"

    pztid = Column(String(50), primary_key=True, index=True)  # ex: 20250330_intern_1
    cpid = Column(String(50), ForeignKey("companies.cpid", ondelete="CASCADE"))
    pztname = Column(String(255), nullable=False)
    pztlevel = Column(String(20))  # Intern, NewGrad, ...
    year = Column(Integer, nullable=False)
    url = Column(Text)
    jd = Column(Text)
    note = Column(Text)
    active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
    updated_by = Column(String(100))
    oa_first = Column(Boolean, default=False)
    deadline = Column(TIMESTAMP, nullable=True)

