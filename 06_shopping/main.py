from fastapi import FastAPI
import uvicorn
from apps.app01.urls import shop
from apps.app02.urls import user

app = FastAPI()

app.include_router(shop, prefix="/shop", tags=["ショップページ"])
app.include_router(user, prefix="/user", tags=["ユーザーページ"])

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
