from sqlalchemy import select, insert, delete, update
from sqlalchemy.orm import Session
from models import Transaction as model
from schemas import TransactionCreate, Transaction
from database import engine
from copy import deepcopy


def get_all():
    with Session(engine) as session:
        return session.scalars(select(model)).all()


def get_by_id(id: int):
    with Session(engine) as session:
        return session.scalar(select(model).where(model.id == id))


def create_one(tr: TransactionCreate):
    with Session(engine) as session:
        new_tr = {
            "concept": tr.concept,
            "category_id": tr.category_id,
            "quantity": tr.quantity,
            "resolved": tr.resolved,
        }
        result = deepcopy(session.scalar(insert(model).returning(model), new_tr))
        session.commit()
        return result


def delete_by_id(id: int):
    with Session(engine) as session:
        result = deepcopy(
            session.scalar(delete(model).where(model.id == id).returning(model))
        )
        session.commit()
        return result


def update_one(tr: Transaction):
    with Session(engine) as session:
        upd_tr = {
            "id": tr.id,
            "concept": tr.concept,
            "category_id": tr.category_id,
            "quantity": tr.quantity,
            "resolved": tr.resolved,
            "created": tr.created,
        }
        result = deepcopy(
            session.scalar(
                update(model).where(model.id == tr.id).values(upd_tr).returning(model)
            )
        )
        session.commit()
        return result
