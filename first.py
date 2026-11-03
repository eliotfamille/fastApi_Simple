from fastapi import FastAPI

First = FastAPI()


@First.get("/")
async def root():
    return {"message": "Hello World"}
