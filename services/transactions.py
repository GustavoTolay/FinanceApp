from sqlalchemy.orm import Session
from models import TransactionModel as Model
from schemas import TransactionCreate, Transaction


def get_all(db: Session):
    return db.query(Model).all()


def get_by_id(db: Session, id: int):
    return db.query(Model).filter(Model.id == id).first()


def create(db: Session, tr: TransactionCreate):
    new_tr = Model(
        concept=tr.concept,
        category=tr.category,
        quantity=tr.quantity,
        resolved=tr.resolved,
    )
    db.add(new_tr)
    db.commit()
    db.refresh(new_tr)
    return new_tr


def delete_by_id(db: Session, id: int):
    db.query(Model).filter(Model.id == id).delete(synchronize_session="fetch")
    db.commit()
    return {"deleted": True}


def update(db: Session, tr: Transaction):
    db.query(Model).filter(Model.id == tr.id).update(
        {
            Model.concept: tr.concept,
            Model.category: tr.category,
            Model.quantity: tr.quantity,
            Model.resolved: tr.resolved,
        },
        synchronize_session="fetch",
    )
    db.commit()
    return db.query(Model).filter(Model.id == tr.id).first()
