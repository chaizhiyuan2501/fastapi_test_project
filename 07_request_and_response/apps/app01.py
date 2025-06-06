from fastapi import APIRouter

app01 = APIRouter()


@app01.get("user")
def get_user():
    return {"user_id": "user_id"}
