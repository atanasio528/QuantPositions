from sqlalchemy import Column, String, Boolean, TIMESTAMP, ForeignKey
from app.database import Base

class Applied(Base):
    __tablename__ = "applied"
    usrid = Column(String(50), ForeignKey("users.usrid", ondelete="CASCADE"), primary_key=True)
    cpid = Column(String(50), ForeignKey("companies.cpid", ondelete="CASCADE"))
    pztid = Column(String(50), ForeignKey("positions.pztid", ondelete="CASCADE"), primary_key=True)
    applied = Column(Boolean, default=False)
    applied_at = Column(TIMESTAMP, nullable=True)
