from fastapi import FastAPI, Depends
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import services.transactions as tr
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
  db = SessionLocal()
  try:
      yield db
  finally:
      db.close()

@app.get("/")
async def root():
  return { "message": "Hi" }

@app.get("/transactions")
async def get_transactions(db: Session = Depends(get_db)):
  return tr.get_all(db)