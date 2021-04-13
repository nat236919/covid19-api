"""
FILE: base_model.py
DESCRIPTION: Models for General Usage
AUTHOR: Nuttaphat Arunoprayoch
DATE: 01-March-2021
"""
# Import libraries
from typing import Any

from pydantic import BaseModel


#######################################
# ResponseModel
#######################################
class ResponseModel(BaseModel):
    data: Any
    dt: str
    ts: int
