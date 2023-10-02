from fastapi import FastAPI
from routers import transactions

app = FastAPI()
app.include_router(transactions.router)

@app.get("/")
async def root() -> dict:
    return {"message": "Hi"}