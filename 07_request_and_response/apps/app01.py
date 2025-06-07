from fastapi import APIRouter

app01 = APIRouter()


# ユーザーIDを取得するエンドポイント
# ルートパラメータidは型指定がないため、どんな値でも受け取ることができます（例: 文字列や数字）。
@app01.get("/user/{id}")
def get_user(id):
    # id = 1
    print(f"User ID: {id}")
    return {"user_id": id}


# 記事IDを取得するエンドポイント
# ルートパラメータidはint型で指定されているため、整数値のみマッチします。
@app01.get("/articles/{id}")
def get_articles(id: int):
    # id = 1
    print(f"articles ID: {id}", type(id))
    return {"articles_id": id}


# --- ルーティングのマッチング順序について ---
# FastAPIでは、ルートは定義された順番でマッチングされます。
# 例えば、/articles/{id}のように型指定（int）がある場合、URLパスが整数のときのみこのルートがマッチします。
# 一方、/user/{id}のように型指定がない場合は、どんな値でもマッチします。
# ルートが重複する場合や、より具体的なパス（型指定や静的パス）が先に定義されていると、そちらが優先されます。
# したがって、似たようなパスを定義する場合は、より具体的なルートを先に書くことが推奨されます。
