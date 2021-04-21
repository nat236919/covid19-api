"""
FILE: covid_api_v1_model.py
DESCRIPTION: Models for API v1
AUTHOR: Nuttaphat Arunoprayoch
DATE: 01-March-2021
"""
# Import libraries
from typing import List

from pydantic import BaseModel

# class model:
#     """
#     The Context defines the interface of interest to clients. It also maintains
#     a reference to an instance of a State subclass, which represents the current
#     state of the Context.
#     """
#
#     _state = None
#     """
#     A reference to the current state of the Context.
#     """
#
#     def __init__(self, state: State) -> None:
#         self.transition_to(state)
#
#     def transition_to(self, state: State):
#         """
#         The Context allows changing the State object at runtime.
#         """
#
#         print(f"Context: Transition to {type(state).__name__}")
#         self._state = state
#         self._state.context = self
#
#     """
#     The Context delegates part of its behavior to the current State object.
#     """
#
#     def request1(self):
#         self._state.handle1()
#
#     def request2(self):
#         self._state.handle2()
#
#
# class State(baseModel):
#     """
#     The base State class declares methods that all Concrete State should
#     implement and also provides a backreference to the Context object,
#     associated with the State. This backreference can be used by States to
#     transition the Context to another State.
#     """
#
#     @property
#     def context(self) -> Context:
#         return self._context
#
#     @context.setter
#     def context(self, context: Context) -> None:
#         self._context = context
#
#     @abstractmethod
#     def handle1(self) -> None:
#         pass
#
#     @abstractmethod
#     def handle2(self) -> None:
#         pass
#

#######################################
# CurrentModel
#######################################
class CurrentModel(BaseModel):
    confirmed: int
    deaths: int
    recovered: int


#######################################
# CurrentListModel
#######################################
class CurrentListModel(BaseModel):
    countries: List[CurrentModel]
    dt: str
    ts: int


#######################################
# TotalModel
#######################################
class TotalModel(BaseModel):
    confirmed: int
    deaths: int
    recovered: int
    dt: str
    ts: int


#######################################
# ConfirmedModel
#######################################
class ConfirmedModel(BaseModel):
    confirmed: int
    dt: str
    ts: int


#######################################
# DeathsModel
#######################################
class DeathsModel(BaseModel):
    deaths: int
    dt: str
    ts: int


#######################################
# RecoveredModel
#######################################
class RecoveredModel(BaseModel):
    recovered: int
    dt: str
    ts: int


#######################################
# CountriesModel
#######################################
class CountriesModel(BaseModel):
    countries: List[str]
    dt: str
    ts: int


#######################################
# TimeSeriesModel
#######################################
class TimeseriesCoordinatesModel(BaseModel):
    Lat: float
    Long: float


class TimeseriesDataModel(BaseModel):
    date: str
    value: int


class TimeseriesModel(BaseModel):
    Province_State: str
    Country_Region: str
    Coordinates: TimeseriesCoordinatesModel
    Data: List[TimeseriesDataModel]
    