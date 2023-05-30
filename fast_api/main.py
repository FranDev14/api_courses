from fastapi import FastAPI
from libs.models import ModelName

# Load FastAPI module
app = FastAPI()


# Init Lesson: Return a simple Hello World
@app.get("/")
async def root():
    return {"message": "Hello World"}


# Parameters Lesson: Add forced type (int) parameter to the get query and return this parameter or an error
@app.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# Models Lesson: Import a models from another module and use it for return data.
@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    # Model created in a module file for better syntax
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    # In this case, we'll use a model class from another file and put it like a parameter
    return {"model_name": model_name, "message": "Have some residuals"}
