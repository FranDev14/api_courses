from enum import Enum


# Class package for models in fastapi lessons
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
