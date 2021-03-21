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

class countries:
    def __init__(self, countries):
        self.countries: List[str]




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
class CurrentListModel:
    def __init__(self, countries, case):
        self.countriesList: countries
        self.caseOBJ: case


#######################################
# TotalModel
#######################################
class TotalModel:
    def __init__(self, confirmed, recovered, deaths, case):
        self.confirmed: confirmed
        self.recovered: recovered
        self.deaths: deaths
        self.caseOBJ: case


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
    def __init__(self, confirmed, case):
        self.confirmed: confirmed
        self.caseOBJ: case


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
    