import os
from fastapi import APIRouter, File, UploadFile, Request
from typing import List

app06 = APIRouter()

# リクエスト情報を取得して返すエンドポイント
@app06.post("/item")
async def post_file(request: Request):
    # リクエストのURLを出力
    print("URL:", request.url)
    # リクエストメソッドを出力
    print("Method:", request.method)
    # ユーザーエージェント（ブラウザ情報など）を出力
    print("Headers:", request.headers.get("user-agent"))
    # クライアントのホスト（IPアドレス）を出力
    print("Client Host:", request.client.host)
    # クライアントのポート番号を出力
    print("Client Port:", request.client.port)
    # クッキー情報を出力
    print("cookies:", request.cookies)

    # 取得したリクエスト情報をJSON形式で返す
    return {
        "url": str(request.url),
        "method": request.method,
        "headers": request.headers.get("user-agent"),
        "client_host": request.client.host,
        "client_port": request.client.port,
        "cookies": request.cookies,
    }
