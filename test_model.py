from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    id: int
    name: str = "chai"

    model_config = ConfigDict(str_max_length=20)


user = User(id="123")

assert user.name == "chai"
assert user.id == 123
assert isinstance(user.id, int)

assert user.model_dump() == {"id": 123, "name": "chai"}


class Model(BaseModel):
    x: int


m = Model(x=1, y="a")
assert m.model_dump() == {"x": 1}
