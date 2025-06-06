from fastapi import APIRouter

user = APIRouter()


@user.post("/user/login")
def user_login():
    return {"user": "login"}


@user.post("/user/logout")
def user_logout():
    return {"user": "logout"}

