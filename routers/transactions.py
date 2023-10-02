from fastapi import APIRouter
from schemas import Transaction, TransactionCreate
import services.transactions as tr

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.get("/", response_model=list[Transaction])
async def get_all_():
    return tr.get_all()


@router.get("/{id}", response_model=Transaction)
async def get_one_transaction(id: int):
    return tr.get_by_id(id)


@router.delete("/{id}", response_model=Transaction)
async def delete_transaction(id: int):
    return tr.delete_by_id(id)


@router.post("/", response_model=Transaction)
async def create_transaction(body: TransactionCreate):
    return tr.create_one(body)


@router.put("/", response_model=Transaction)
async def update_transaction(body: Transaction):
    return tr.update_one(body)
