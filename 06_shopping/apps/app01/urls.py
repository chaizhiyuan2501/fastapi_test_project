from fastapi import APIRouter

shop = APIRouter()

@shop.get("/shop/food")
def shop_food():
    return {"shop": "food"}


@shop.get("/shop/bed")
def shop_bed():
    return {"shop": "bed"}