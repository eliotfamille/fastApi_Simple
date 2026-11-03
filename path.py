from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


Path = FastAPI()


@Path.get("/models/{name}")
async def get_model(name: ModelName):
    if name is ModelName.alexnet:
        return {"model_name": name, "message": "Deep Learning FTW!"}

    if name.value == "lenet":
        return {"name": name, "message": "LeCNN all the images"}

    return {"name": name, "message": "Have some residuals"}

# prend un chemin url
@Path.get("files/{file_path:path}")
async def read_file(file_path: str):
    return {"fille_path" : file_path}
