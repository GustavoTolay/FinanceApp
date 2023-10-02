from pydantic import BaseModel
from datetime import date

# pydantic models

class TransactionBase(BaseModel):
    concept: str
    category_id: int
    quantity: int
    resolved: bool


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int
    created: date

    class Config:
        orm_mode = True
