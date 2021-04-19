"""
FILE: covid_api_v2_model.py
DESCRIPTION: Models for API v2
AUTHOR: Nuttaphat Arunoprayoch
DATE: 01-March-2021
"""
# Import libraries
from typing import List

from pydantic import BaseModel
from abc import ABC, abstractmethod
from __future__ import annotations


class Models:
    """
    This ModelState defines the interface of interest to clients. It also maintains
    a reference to an instance of a BaseModel subclass, which represents the current
    state of the ModelState.
    """

    _modelState = None
    """
      A reference to the current state of the Context.
    """

    def __init__(self, modelstate: ModelState) -> None:
        self.transition_to(modelstate)

    def transition_to(self, modelstate: ModelState):
        """
        The Models allows changing the BaseModel object at runtime.
        """

        self._modelState = modelstate

    def return_model(self) -> BaseModel:
        """
        The Models return the specific model that the client wants to use.
        """
        return self._modelState.show_model()


class ModelState(BaseModel):
    """
    The base ModelState class declares methods that all Concrete Model should
    implement and also provides a backreference to the Models object,
    associated with the ModelState. This backreference can be used by ModelState to
    transition the Models to another ModelState.
    """

    @property
    def model(self) -> Models:
        return self._model

    @model.setter
    def model(self, model: Models) -> None:
        self._model = model

    @abstractmethod
    def show_model(self) -> BaseModel:
        pass


#######################################
# CurrentModel
#######################################
class CurrentModel(ModelState):
    location: str
    confirmed: int
    deaths: int
    recovered: int
    active: int

    def show_model(self) -> BaseModel:
        return self

#######################################
# CurrentUSModel
#######################################
class CurrentUSModel(ModelState):
    Province_State: str
    Confirmed: int
    Deaths: int
    Recovered: int
    Active: int

    def show_model(self) -> BaseModel:
        return self


#######################################
# TotalModel
#######################################
class TotalModel(ModelState):
    confirmed: int
    deaths: int
    recovered: int
    active: int

    def show_model(self) -> BaseModel:
        return self


#######################################
# ConfirmedModel
#######################################
class ConfirmedModel(ModelState):
    confirmed: int

    def show_model(self) -> BaseModel:
        return self


#######################################
# DeathsModel
#######################################
class DeathsModel(ModelState):
    deaths: int

    def show_model(self) -> BaseModel:
        return self


#######################################
# RecoveredModel
#######################################
class RecoveredModel(ModelState):
    recovered: int

    def show_model(self) -> BaseModel:
        return self


#######################################
# ActiveModel
#######################################
class ActiveModel(ModelState):
    active: int

    def show_model(self) -> BaseModel:
        return self


#######################################
# CountryModel
#######################################
class CountryModel(ModelState):
    location: str
    confirmed: int
    deaths: int
    recovered: int
    active: int

    def show_model(self) -> BaseModel:
        return self


#######################################
# TimeseriesGlobalModel
#######################################
class TimeseriesGlobalModel(BaseModel):
    confirmed: int
    deaths: int
    recovered: int


#######################################
# TimeseriesCaseModel
#######################################
class TimeseriesCaseCoordinatesModel(BaseModel):
    Lat: float
    Long: float


class TimeseriesCaseDataModel(BaseModel):
    date: str
    value: int


class TimeseriesCaseModel(BaseModel):
    Province_State: str
    Country_Region: str
    Coordinates: TimeseriesCaseCoordinatesModel
    TimeSeries: List[TimeseriesCaseDataModel]


#######################################
# TimeseriesUSModel
#######################################
class TimeseriesUSInfoModel(BaseModel):
    UID: str
    iso2: str
    iso3: str
    code3: str
    FIPS: str
    Admin2: str


class TimeseriesUSCoordinatesModel(BaseModel):
    Lat: float
    Long: float


class TimeseriesUSDataModel(BaseModel):
    date: str
    value: int


class TimeseriesUSModel(BaseModel):
    Province_State: str
    Country_Region: str
    Info: TimeseriesUSInfoModel
    Coordinates: TimeseriesUSCoordinatesModel
    TimeSeries: List[TimeseriesUSDataModel]
