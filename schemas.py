from pydantic import BaseModel
from datetime import date


class TransactionBase(BaseModel):
    concept: str
    category: str
    quantity: int
    resolved: bool


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int
    created: date

    class Config:
        orm_mode = True
