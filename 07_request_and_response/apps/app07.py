import os
from fastapi import APIRouter, File, UploadFile, Request
from typing import List
from pydantic import BaseModel
from pydantic.networks import EmailStr
from typing import Union

app07 = APIRouter()


class UserIn(BaseModel):
    Username: str
    Password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    Username: str
    email: EmailStr
    full_name: Union[str, None] = None


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = 10.5
    tags: List[str] = []


items = {
    "item0": {"name": "Item 0", "price": 1.5},
    "item1": {
        "name": "Item 1",
        "description": "Description of Item 1",
        "price": 10.0,
        "tax": 1.0,
        "tags": ["tag1", "tag2"],
    },
    "item2": {
        "name": "Item 2",
        "description": "Description of Item 2",
        "price": 20.0,
        "tax": 2.0,
        "tags": ["tag3", "tag4"],
    },
}

# ユーザー情報を受け取り、パスワードを除いた情報を返すエンドポイント
# リクエストボディはUserIn型、レスポンスはUserOut型
@app07.post("/userIn", response_model=UserOut)
async def create_user(user: UserIn):
    # UserInの内容をそのまま返すが、UserOutで定義されていないPasswordは自動的に除外される
    return user

# 商品IDを指定して商品情報を返すエンドポイント
# レスポンスモデルはItem型、未設定項目は除外（response_model_exclude_unset=True）
@app07.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def create_item(item_id: str):
    # items辞書からitem_idに該当する商品情報を返す
    return items[item_id]
