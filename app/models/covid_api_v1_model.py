"""
FILE: covid_api_v1_model.py
DESCRIPTION: Models for API v1
AUTHOR: Nuttaphat Arunoprayoch
DATE: 01-March-2021
"""
# Import libraries
from typing import List

from pydantic import BaseModel


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
    type: str
    script: int


#######################################
# TotalModel
#######################################
class TotalModel(BaseModel):
    confirmed: int
    deaths: int
    recovered: int
    type: str
    script: int


#######################################
# ConfirmedModel
#######################################
class ConfirmedModel(BaseModel):
    confirmed: int
    type: str
    script: int


#######################################
# DeathsModel
#######################################
class DeathsModel(BaseModel):
    deaths: int
    type: str
    script: int


#######################################
# RecoveredModel
#######################################
class RecoveredModel(BaseModel):
    recovered: int
    type: str
    script: int


#######################################
# CountriesModel
#######################################
class CountriesModel(BaseModel):
    countries: List[str]
    type: str
    script: int


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
    
