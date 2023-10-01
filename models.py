from sqlalchemy import Boolean, Column, Integer, String, Date
from datetime import date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import Optional, List

class Base(DeclarativeBase):
    pass

class TransactionModel(Base):
    __tablename__ = "transactions"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    concept: Mapped[str] = mapped_column(String)
    # category: Mapped["Category"] = relationship()
    quantity: Mapped[int] = mapped_column(Integer)
    resolved: Mapped[bool] = mapped_column(Boolean, default=False)
    created: Mapped[date] = mapped_column(Date, default=date.today())
    
    # def __repr__(self) -> str:
        # return f"User(id={self.id!r}, concept={self.concept!r}, category={self.category!r})"