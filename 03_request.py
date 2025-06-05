from fastpi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/get")
def get_test():
    return {"method":"getメソッド"}
@app.post("/post")
def post_test():
    return {"method":"postメソッド"}
@app.put("/put")
def put_test():
    return {"method":"putメソッド"}
@app.delete("/delete")
def delete_test():
    return {"method":"deleteメソッド"}



if __name__ == "__main__":
    uvicorn.run("03_request:app",port=8000,debug=True,reload=True)
