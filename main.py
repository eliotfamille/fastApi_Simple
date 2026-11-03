from fastapi import FastAPI

app = FastAPI()


@app.get("/item")
async def root():
    return {"message" }
