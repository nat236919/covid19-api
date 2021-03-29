"""
FILE: base_model.py
DESCRIPTION: Models for General Usage
AUTHOR: Nuttaphat Arunoprayoch
DATE: 01-March-2021
"""
# Import libraries
from typing import Any, Dict, List

from pydantic import BaseModel


#######################################
# ResponseModel
#######################################
class ResponseModel(BaseModel):
    _instance: None
    data: Any
    dt: str
    ts: int


def __init__(self):
    self.dt = 'Unknown'
    self.ts = 0


def get_instance(self):
    if self._instance is None:
        self.instance = BaseModel
    else:
        return self._instance

