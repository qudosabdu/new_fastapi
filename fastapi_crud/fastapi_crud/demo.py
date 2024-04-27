from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Hello World from Home Page"}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# @app.get("/items")
# async def hello(query: str = None, page: int = 10):
#     return {"message": "Hello World from Items Page", "query": query, "page": page}


# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]


# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}

# http://127.0.0.1:8000/items/5?q=hello
# Output: {"item_id": "5", "q": "hello"}


# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(
#     user_id: int, item_id: str, q: str | None = None, short: bool = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

# http://127.0.0.1:8000/users/100/items/101
# Output: {"item_id": "101", "owner_id": 100, "description": "This is an amazing item that has a long description"}


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

# http://127.0.0.1:8000/items/foo-item?needy=sooooneedy
# Output: {"item_id": "foo-item", "needy": "sooooneedy"}