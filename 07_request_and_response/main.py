from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
from apps.app01 import app01
from apps.app02 import app02
from apps.app03 import app03
from apps.app04 import app04
from apps.app05 import app05
from apps.app06 import app06
from apps.app07 import app07

app = FastAPI()

app.mount("/static", StaticFiles(directory="07_request_and_response/static"))

app.include_router(app01, prefix="/user", tags=["01 パスパラメーター"])
app.include_router(app02, prefix="/job", tags=["02 クエリパラメータ"])
app.include_router(app03, prefix="/user", tags=["03 リクエストボディパラメーター"])
app.include_router(app04, prefix="/user", tags=["04 フォームのフォーマット"])
app.include_router(app05, prefix="/file", tags=["05 ファイルのアップロード"])
app.include_router(app06, prefix="/request", tags=["06 リクエスト対象"])
app.include_router(app07, prefix="/request", tags=["07 响应参数"])

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
