from typing import Dict
from typing import List

from fastapi import APIRouter
from fastapi import HTTPException

from src.schemas.lamoda import Product
from src.services import controller


router = APIRouter(tags=["Lamoda"], prefix="/lamoda")


@router.get("/products", response_model=List[Product])
async def get_product_list():
    return controller.lamoda.list_products()


@router.post("/products")
async def create_product(data: Product):
    return controller.lamoda.create_product(data)


@router.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: str):
    product = controller.lamoda.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Item not found")
    return product


@router.patch("/products/{product_id}", response_model=Product)
async def update_product(product_id: str, data: Dict):
    return controller.lamoda.update_product(product_id, data)


@router.delete("/products/{product_id}")
async def delete_product(product_id: str) -> Dict:
    return controller.lamoda.delete_object(product_id)
