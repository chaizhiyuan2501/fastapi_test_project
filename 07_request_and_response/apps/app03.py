from fastapi import APIRouter
from datetime import date
from pydantic import BaseModel
from typing import List

app03 = APIRouter()


class User(BaseModel):
    name: str
    age: int
    email: str
    birthday: date
    friends: List[int] = []  # デフォルト値として空のリストを設定


# ジョブ情報を取得するエンドポイント
# job_type: パスパラメータ。職種を表す文字列。デフォルト値は"all"。
# limit: クエリパラメータ。取得する件数の上限。int型またはNoneを許容。デフォルト値は10。
# salary: クエリパラメータ。給与でフィルタリングする場合に使用。int型またはNoneを許容。デフォルト値はNone。
#
# typing.Optional（ここではopt）は「指定した型またはNone」を意味し、例えばopt[int]は「int型またはNone」を許容します。
# typing.Union（ここではuni）は「複数の型のいずれか」を意味し、例えばuni[int, None]は「int型またはNone」を許容します。
# 実際にはopt[int]はuni[int, None]と同じ意味になります。
@app03.post("/data")
async def post_data(data: User):
    return {}
