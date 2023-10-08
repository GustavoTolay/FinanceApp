from pydantic import BaseModel
from datetime import date

# pydantic models


class TransactionBase(BaseModel):
    concept: str
    category_id: int
    quantity: int
    is_income: bool
    resolved: bool


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int
    created: date

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


# response models
class TransactionJoin(Transaction):
    category: Category
    
