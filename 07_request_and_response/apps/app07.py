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

# response_model_exclude関連の主なパラメータとその説明

# response_model_include（白名单）
# レスポンスモデルに含めたいフィールド名をリストやセットで指定します。

# response_model_exclude（黑名单）
# レスポンスモデルから除外したいフィールド名をリストやセットで指定します。
# 例: response_model_exclude={"tax", "tags"}
# 指定したフィールドはレスポンスから除外されます。

# response_model_exclude_unset
# デフォルト値のまま（未設定）のフィールドをレスポンスから除外するかどうかを指定します。
# Trueにすると、リクエストで値が設定されていないフィールドはレスポンスに含まれません。
# 例: response_model_exclude_unset=True

# response_model_exclude_defaults
# モデルで定義されたデフォルト値と同じ値のフィールドをレスポンスから除外するかどうかを指定します。
# Trueにすると、デフォルト値と同じ値のフィールドはレスポンスに含まれません。
# 例: response_model_exclude_defaults=True

# response_model_exclude_none
# Noneの値を持つフィールドをレスポンスから除外するかどうかを指定します。
# Trueにすると、値がNoneのフィールドはレスポンスに含まれません。
# 例: response_model_exclude_none=True
