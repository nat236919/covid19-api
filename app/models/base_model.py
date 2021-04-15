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
    data: Any
    type: str
    script: int

class ResponseModel(BaseModel):
   __instance__ = None

   def __init__(self):
       """ Private constructor. """
       if ResponseModel.__instance__ is None:
           ResponseModel.__instance__ = self
       else:
           raise Exception("Sorry you can't create another ResponseModel class")

   @staticmethod
   def get_instance():
       """ A static method that will call the created instance."""
       if not ResponseModel.__instance__:
           ResponseModel()
       return ResponseModel.__instance__
a
