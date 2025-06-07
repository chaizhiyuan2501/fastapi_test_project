from fastapi import APIRouter
from typing import (
    Union as uni,
)  # Unionは複数の型を許容するための型ヒント。ここではエイリアスとしてuniを使用。
from typing import (
    Optional as opt,
)  # Optionalは「Noneも許容する型」を表す型ヒント。ここではエイリアスとしてoptを使用。

app02 = APIRouter()


# ジョブ情報を取得するエンドポイント
# job_type: パスパラメータ。職種を表す文字列。デフォルト値は"all"。
# limit: クエリパラメータ。取得する件数の上限。int型またはNoneを許容。デフォルト値は10。
# salary: クエリパラメータ。給与でフィルタリングする場合に使用。int型またはNoneを許容。デフォルト値はNone。
#
# typing.Optional（ここではopt）は「指定した型またはNone」を意味し、例えばopt[int]は「int型またはNone」を許容します。
# typing.Union（ここではuni）は「複数の型のいずれか」を意味し、例えばuni[int, None]は「int型またはNone」を許容します。
# 実際にはopt[int]はuni[int, None]と同じ意味になります。
@app02.get("/jobs/{job_type}")
async def get_jobs(
    job_type: str = "all", limit: opt[int] = 10, salary: uni[int, None] = None
):
    return {
        "msg": "this is get_jobs",
        "job_type": job_type,
        "limit": limit,
        "salary": salary,
    }
