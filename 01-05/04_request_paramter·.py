from fastpi import FastAPI
import uvicorn

app = FastAPI()


@app.post(
    "/items",
    tags=["itemsのテストポート"],
    summary="this is summary",
    description="this is items test description",
    response_description="this is items test response_description",
    deprecated=True,
)
def post_test():
    return {"items": "itemsパラメーター"}


if __name__ == "__main__":
    uvicorn.run("03_request:app", port=8000, debug=True, reload=True)
