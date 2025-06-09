from fastapi import APIRouter
from datetime import date
from pydantic import BaseModel, Field, field_validator
from typing import List, Union, Optional

app03 = APIRouter()


class Address(BaseModel):
    province: str
    city: str


class User(BaseModel):
    name: str = Field(pattern="[a-zA-Z]{1,20}")  # 名前は1〜20文字の英字
    age: int = Field(default=18, gt=0, lt=120)  # 年齢は1以上120以下
    email: str
    birthday: Union[date, None] = None  # 誕生日はdate型またはNoneを許容
    friends: List[int] = []  # デフォルト値として空のリストを設定
    description: Optional[str] = None  # 説明は文字列またはNoneを許容
    address: Optional[Address] = None  # 住所はAddress型またはNoneを許容

    @field_validator("name")
    def name_must_alphabet(cls, value):
        assert value.isalpha(), "名前は英字のみでなければなりません"
        return value


class Data(BaseModel):
    data: List[User]


# ジョブ情報を取得するエンドポイント
# job_type: パスパラメータ。職種を表す文字列。デフォルト値は"all"。
# limit: クエリパラメータ。取得する件数の上限。int型またはNoneを許容。デフォルト値は10。
# salary: クエリパラメータ。給与でフィルタリングする場合に使用。int型またはNoneを許容。デフォルト値はNone。
#
# typing.Optional（ここではopt）は「指定した型またはNone」を意味し、例えばopt[int]は「int型またはNone」を許容します。
# typing.Union（ここではuni）は「複数の型のいずれか」を意味し、例えばuni[int, None]は「int型またはNone」を許容します。
# 実際にはopt[int]はuni[int, None]と同じ意味になります。

# @app03.post("/data")
# async def post_data(user: User):
#     print(user, type(user))
#     print(user.model_dump())
#     # ここでは受け取ったデータをそのまま返す
#     return user


@app03.post("/data")
async def post_data(data: Data):
    # ここでは受け取ったデータをそのまま返す
    return data
