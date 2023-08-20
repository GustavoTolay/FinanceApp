from sqlalchemy import Boolean, Column, Integer, String, Date
from datetime import date

from database import Base

class Transaction(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    concept = Column(String)
    category = Column(String)
    quantity = Column(Integer)
    resolved = Column(Boolean, default=False)
    created = Column(Date, default=date.today())
