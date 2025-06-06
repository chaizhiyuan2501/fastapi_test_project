from fastapi import FastAPI
import uvicorn

from apps.app01 import app01

app = FastAPI()

app.include_router(app01, prefix="/user", tags=["パスパラメーター"])

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
