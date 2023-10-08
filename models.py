from sqlalchemy import Boolean, Integer, String, Date, ForeignKey
from datetime import date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List

# SQLAlchemy models

class Base(DeclarativeBase):
    pass

class Transaction(Base):
    __tablename__ = "transaction"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    concept: Mapped[str] = mapped_column(String)
    category: Mapped["Category"] = relationship(back_populates="transactions")
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    quantity: Mapped[int] = mapped_column(Integer)
    is_income: Mapped[bool] = mapped_column(Boolean)
    resolved: Mapped[bool] = mapped_column(Boolean, default=False)
    created: Mapped[date] = mapped_column(Date, default=date.today())
    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, concept={self.concept!r}, quantity={self.quantity!r}, is_income={self.is_income!r}, resolved={self.quantity!r}, created={self.created!r})"
        
class Category(Base):
    __tablename__ = "category"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    transactions: Mapped[List["Transaction"]] = relationship(back_populates="category")
    
    def __repr__(self) -> str:
        return f"Category(id={self.id!r}, name={self.name!r})"
    