from sqlalchemy import select, insert, delete, update
from sqlalchemy.orm import Session, joinedload
from models import Transaction as model
from schemas import TransactionCreate, Transaction
from database import engine
from copy import deepcopy
from fastapi import HTTPException

err_404 = HTTPException(status_code=404, detail="Transaction not found")


def get_all():
    # with statement needed so the session closes everytime
    with Session(engine) as session:
        query = select(model).options(joinedload(model.category))
        return session.scalars(query).all()
        # without commit() engine rollbacks everytime


def get_by_id(id: int):
    with Session(engine) as session:
        query = select(model).options(joinedload(model.category)).where(model.id == id)
        result = session.scalar(query)
        if result:
            return result
        raise err_404


def create_one(tr: TransactionCreate):
    with Session(engine) as session:
        new_tr = {
            "concept": tr.concept,
            "category_id": tr.category_id,
            "quantity": tr.quantity,
            "is_income": tr.is_income,
            "resolved": tr.resolved,
        }
        # Deep copy for clone result before it gets flushed by commit()
        result = deepcopy(session.scalar(insert(model).returning(model), new_tr))
        session.commit()
        if result:
            return result
        raise err_404


def delete_by_id(id: int):
    with Session(engine) as session:
        result = deepcopy(
            session.scalar(delete(model).where(model.id == id).returning(model))
        )
        session.commit()
        if result:
            return result
        raise err_404


def update_one(tr: Transaction):
    with Session(engine) as session:
        upd_tr = {
            "id": tr.id,
            "concept": tr.concept,
            "category_id": tr.category_id,
            "quantity": tr.quantity,
            "is_income": tr.is_income,
            "resolved": tr.resolved,
            "created": tr.created,
        }
        result = deepcopy(
            session.scalar(
                update(model).where(model.id == tr.id).values(upd_tr).returning(model)
            )
        )
        session.commit()
        if result:
            return result
        raise err_404
