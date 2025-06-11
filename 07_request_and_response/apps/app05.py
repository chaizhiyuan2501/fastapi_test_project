import os
from fastapi import APIRouter, File, UploadFile
from typing import List

app05 = APIRouter()


@app05.post("/file")
async def post_file(file: bytes = File()):
    print("file", file)
    return {"file": len(file), "message": "File uploaded successfully"}


@app05.post("/files")
async def post_files(files: List[bytes] = File()):
    for file in files:
        print((len(file)))
    return {"files": len(files), "message": "Files uploaded successfully"}


@app05.post("/uploadfile")
async def get_update_file(file: UploadFile):
    # imgsディレクトリが存在しない場合は作成
    os.makedirs("07_request_and_response/imgs", exist_ok=True)

    path = os.path.join("07_request_and_response/imgs", file.filename)
    with open(path, "wb") as f:
        for line in file.file:
            f.write(line)
    return {"filename": file.filename, "message": "File uploaded successfully"}


@app05.post("/uploadfile")
async def get_update_files(files: List[UploadFile]):
    # imgsディレクトリが存在しない場合は作成
    # （ここではファイル保存処理は省略）
    return {"filename": [file.filename for file in files]}
