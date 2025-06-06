from pydantic import BaseModel, ConfigDict


# ユーザーモデルを定義する。BaseModel を継承することで、型バリデーションなどの機能が使える。
class User(BaseModel):
    id: int  # ユーザーID：整数型
    name: str = "chai"  # 名前：デフォルト値 "chai"

    # モデル設定：文字列の最大長を 20 に制限
    model_config = ConfigDict(str_max_length=20)


# User モデルのインスタンスを作成。id に文字列を渡しても int に変換される（Pydantic の型強制機能）。
user = User(id="123")

# デフォルト値のテスト
assert user.name == "chai"
# 型変換されたか確認
assert user.id == 123
assert isinstance(user.id, int)

# モデルを辞書形式で出力して確認
assert user.model_dump() == {"id": 123, "name": "chai"}


# 入れ子構造（ネスト）を持つモデルの定義
class Foo(BaseModel):
    count: int  # 必須フィールド
    size: float | None = None  # オプションの浮動小数点型


class Bar(BaseModel):
    apple: str = "x"  # デフォルト値付きフィールド
    banana: str = "y"


class Spam(BaseModel):
    foo: Foo  # Foo 型のフィールド
    bars: list[Bar]  # Bar のリスト


# Foo と Bar に辞書形式でデータを渡してインスタンスを作成（自動的にネストされたモデルに変換される）
m = Spam(foo={"count": 4}, bars=[{"apple": "x1"}, {"apple": "x2"}])

# モデルの出力（__str__ の結果）を表示
print(m)

# model_dump() により、辞書形式で全体を出力
print(m.model_dump())
