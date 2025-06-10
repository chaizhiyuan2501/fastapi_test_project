from fastapi import FastAPI
import uvicorn

from apps.app01 import app01
from apps.app02 import app02
from apps.app03 import app03
from apps.app04 import app04

app = FastAPI()

app.include_router(app01, prefix="/user", tags=["01 パスパラメーター"])
app.include_router(app02, prefix="/job", tags=["02 クエリパラメータ"])
app.include_router(app03, prefix="/user", tags=["03 リクエストボディパラメーター"])
app.include_router(app04, prefix="/user", tags=["04 フォームのフォーマット"])

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
