from fastapi import FastAPI
from schemas import TransactionCreate, Transaction
import services.transactions as tr

app = FastAPI()

@app.get("/")
async def root() -> dict:
    return {"message": "Hi"}


@app.get("/transactions", response_model=list[Transaction])
async def get_all_transactions():
    return tr.get_all()


@app.get("/transactions/{id}", response_model=Transaction)
async def get_one_transaction(id: int):
    return tr.get_by_id(id)


@app.delete("/transactions/{id}")
async def delete_transaction(id: int):
    return tr.delete_by_id(id)


@app.post("/transactions", response_model=Transaction)
async def create_transaction(body: TransactionCreate):
    return tr.create_one(body)


@app.put("/transactions", response_model=Transaction)
async def update_transaction(body: Transaction):
    return tr.update_one(body)
