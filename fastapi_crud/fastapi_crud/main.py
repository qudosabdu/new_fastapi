from fastapi import FastAPI

app = FastAPI()

@app.get("/about")
async def root():
    return {"message": "Hello from FastAPI!"}
