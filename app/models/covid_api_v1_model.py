"""
FILE: covid_api_v1_model.py
DESCRIPTION: Models for API v1
AUTHOR: Nuttaphat Arunoprayoch
DATE: 01-March-2021
"""
# Import libraries
from typing import List
from models import cases
from pydantic import BaseModel]

class case:
    def __init__(self, dt, ts):
        self.dt: str
        self.ts: int





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
class ConfirmedModel:
    def __init__(self, confirmed, case):
        self.confirmed: confirmed
        self.caseOBJ: case
    



#######################################
# DeathsModel
#######################################
class DeathsModel:
    def __init__(self, deaths, case):
        self.deathCases: deaths
        self.caseOBJ: case


#######################################
# RecoveredModel
#######################################
class RecoveredModel:
    def __init__(self, recovered, case):
        self.recoveredCases: recovered
        self.caseOBJ: case
    


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
    