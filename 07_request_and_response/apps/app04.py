from fastapi import APIRouter, Form

app04 = APIRouter()


# ユーザー登録用のエンドポイント
# フォームデータとしてusernameとpasswordを受け取る
@app04.post("/regin")
async def regin(username: str = Form(), password: str = Form()):
    print(f"Received username: {username}, password: {password}")
    return {"username": username, "password": password}
