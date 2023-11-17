# When you declare other function parameters that are not part of the path parameters,\
# they are automatically interpreted as "query" parameters.

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int, limit: int = 10, val: None = None): # val is no required, skip is required, limit is defalt variable and no required
    return fake_items_db[skip : skip + limit]
