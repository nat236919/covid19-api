"""
FILE: covid_api_v3_adapter.py
DESCRIPTION: Models for API v3
AUTHOR: Nuttaphat Arunoprayoch
DATE: 15-March-2021
"""
# Import libraries
import pandas as pd

import models.covid_model_api_v1

import models.covid_model_api_v2

from typing import List, Any, Dict

from pydantic import BaseModel

from structural import time_data

from utils.get_data import get_data


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

class version3Adapter:
    def __init(self):
        self.version1 = CovidAPIv1()
        self.version2 = CovidAPIv2()

    def get_time_series(self, v):
        if v == 1:
            version1.get_time_series()
        if v == 2: 
            version2.get_time_series()