from fastapi import FastAPI, Depends
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import services.transactions as tr
from models import Base
from schemas import TransactionCreate, Transaction

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def ss():
    return Depends(get_db)


@app.get("/")
async def root() -> dict:
    return {"message": "Hi"}


@app.get("/transactions", response_model=list[Transaction])
async def get_all_transactions(db: Session = ss()):
    return tr.get_all(db)


@app.get("/transactions/{id}", response_model=Transaction)
async def get_one_transaction(id: int, db: Session = ss()):
    return tr.get_by_id(db, id)


@app.delete("/transactions/{id}")
async def delete_transaction(id: int, db: Session = ss()) -> dict:
    return tr.delete_by_id(db, id)


@app.post("/transactions", response_model=Transaction)
async def create_transaction(body: TransactionCreate, db: Session = ss()):
    return tr.create(db, body)


@app.put("/transactions", response_model=Transaction)
async def update_transaction(body: Transaction, db: Session = ss()):
    return tr.update(db, body)
