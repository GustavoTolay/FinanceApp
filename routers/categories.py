from fastapi import APIRouter
from schemas import Category, CategoryCreate
import services.categories as cat

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=list[Category])
async def get_all_():
    return cat.get_all()


@router.get("/{id}", response_model=Category)
async def get_one_category(id: int):
    return cat.get_by_id(id)


@router.delete("/{id}", response_model=Category)
async def delete_category(id: int):
    return cat.delete_by_id(id)


@router.post("/", response_model=Category)
async def create_category(body: CategoryCreate):
    return cat.create_one(body)


@router.put("/", response_model=Category)
async def update_category(body: Category):
    return cat.update_one(body)