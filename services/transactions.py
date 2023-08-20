from sqlalchemy.orm import Session
from ..models import Transaction

def get_transaction_by_id(db: Session, id: int):
  return db.query(Transaction).filter(Transaction.id == id).first()