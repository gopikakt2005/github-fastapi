from fastapi import FastAPI

# Initialize the FastAPI app
app = FastAPI()

# A basic GET route at the root ("/")
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# A GET route with a path parameter and query parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "query": q}