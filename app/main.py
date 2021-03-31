"""
PROJECT: COVID19-API
DESCRIPTION: Daily level information on various cases
AUTHOR: Nuttaphat Arunoprayoch
DATE: 9-Feb-2020
RUN SERVER: uvicorn main:app --reload
"""
# Import libraries
import sys
from functools import wraps
from typing import Any, Dict

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from config import CONFIG
from routers.v1 import v1
from routers.v2 import v2

from abc import ABCMeta, abstractmethod


# Setup application
# Note: Please visit config.py for modification
app = FastAPI(
    title=CONFIG['app'].get('title'),
    description=CONFIG['app'].get('description'),
    version=CONFIG['app'].get('version')
)

# Setup CORS (https://fastapi.tiangolo.com/tutorial/cors/)
# Note: Wild-card setup is used here for demonstration only,
#       Please change the setting in accordance with your application
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


"""
SECTION: Default route
DESCRIPTION: Route to API documentation
"""
# API documentation
@app.get('/', include_in_schema=False)
def read_docs() -> None:
    """ API documentation """
    return RedirectResponse(url='/docs')

class IBuilder(metaclass=ABCMeta):
    "The Builder Interface"

    @staticmethod
    @abstractmethod
    def build_router_v1():
        "Builds router v1"

    @staticmethod
    @abstractmethod
    def build_router_v2():
        "Builds router v2"
class Builder(IBuilder):
    "The Concrete Builder."

    def __init__(self):
        self.routes = []

    def build_router_v1(self):
        self.routes.append('v1')
        app.include_router(v1, prefix="", tags=["v1"])
        return self

    def build_router_v2(self):
        self.routes.append('v2')
        app.include_router(v2, prefix="/v2", tags=["v2"])
        return self

class Director:
    "The Director, building a complex representation."

    @staticmethod
    def construct():
        "Constructs and returns the final product"
        return Builder()\
            .build_router_v2()\
            .build_router_v1()


ROUTES = Director.construct()
