from fastapi import FastAPI
import uvicorn

from apps.app01 import app01
from apps.app02 import app02

app = FastAPI()

app.include_router(app01, prefix="/user", tags=["01 パスパラメーター"])
app.include_router(app02, prefix="/user", tags=["02 クエリパラメータ"])

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
