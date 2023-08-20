from fastapi import FastAPI
from services.transactions import get_transaction_by_id

app = FastAPI()

@app.get("/")
async def root():
  return { "message": "Hi" }

@app.get("/transactions")
async def getTransactions():
  return get_transaction_by_id