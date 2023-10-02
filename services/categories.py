from sqlalchemy import select, insert, delete, update
from sqlalchemy.orm import Session
from models import Category as model
from schemas import Category, CategoryCreate
from database import engine
from copy import deepcopy


def get_all():
    with Session(engine) as session:
        return session.scalars(select(model)).all()


def get_by_id(id: int):
    with Session(engine) as session:
        return session.scalar(select(model).where(model.id == id))


def create_one(cat: CategoryCreate):
    with Session(engine) as session:
        new_cat = {"name": cat.name}
        result = deepcopy(session.scalar(insert(model).returning(model), new_cat))
        session.commit()
        return result


def delete_by_id(id: int):
    with Session(engine) as session:
        result = deepcopy(
            session.scalar(delete(model).where(model.id == id).returning(model))
        )
        session.commit()
        return result


def update_one(cat: Category):
    with Session(engine) as session:
        upd_cat = {"id": cat.id, "name": cat.name}
        result = deepcopy(
            session.scalar(
                update(model).where(model.id == cat.id).values(upd_cat).returning(model)
            )
        )
        session.commit()
        return result
