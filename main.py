from fastapi import FastAPI
from schemas import TransactionCreate, Transaction
from routers import transactions
import services.transactions as tr

app = FastAPI()
app.include_router(transactions.router)

@app.get("/")
async def root() -> dict:
    return {"message": "Hi"}