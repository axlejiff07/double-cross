from fastapi import FastAPI

app = FastAPI()

"""Fast API root route"""
@app.get("/")
async def root():
    # check http://127.0.0.1:8000/
    # check http://127.0.0.1:8000/docs
    # check http://127.0.0.1:8000/redoc
    # check http://127.0.0.1:8000/openapi.json
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    # check http://127.0.0.1:8000/items/id/foo
    return {"item_id": item_id}

@app.get("/items/id/{item_id}")
async def read_item(item_id: int):
    # check http://127.0.0.1:8000/items/id/12
    # check http://127.0.0.1:8000/items/id/foo
    return {"item_id": item_id}

@app.get("/users/me")
async def read_user_me():
    # check http://127.0.0.1:8000/users/me
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    # check http://127.0.0.1:8000/users/me
    # check http://127.0.0.1:8000/users/12
    return {"user_id": user_id}