from sqlalchemy.orm import Session
from models import Transaction

def get_all(db: Session):
  return db.query(Transaction)

def get_by_id(db: Session, id: int):
  return db.query(Transaction).filter(Transaction.id == id).first()