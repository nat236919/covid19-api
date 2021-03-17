"""
FILE: covid_api_v1_model.py
DESCRIPTION: Models for API v1
AUTHOR: Nuttaphat Arunoprayoch
DATE: 01-March-2021
"""
# Import libraries
from typing import List

from pydantic import BaseModel

from aggregates import time-data

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
    td: TimeData


#######################################
# TotalModel
#######################################
class TotalModel(BaseModel):
    confirmed: int
    deaths: int
    recovered: int
    td: TimeData


#######################################
# ConfirmedModel
#######################################
class ConfirmedModel(BaseModel):
    confirmed: int
    td: TimeData


#######################################
# DeathsModel
#######################################
class DeathsModel(BaseModel):
    deaths: int
    td: TimeData


#######################################
# RecoveredModel
#######################################
class RecoveredModel(BaseModel):
    recovered: int
    td: TimeData


#######################################
# CountriesModel
#######################################
class CountriesModel(BaseModel):
    countries: List[str]
    td: TimeData


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
    