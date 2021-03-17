"""
FILE: covid_api_v2_model.py
DESCRIPTION: Models for API v2
AUTHOR: Nuttaphat Arunoprayoch
DATE: 01-March-2021
"""
# Import libraries
from typing import List

from pydantic import BaseModel

#######################################
# CurrentModel
#######################################
class CurrentModel(BaseModel): #changes made right here
    location: str
    confirmed: int
    deaths: int
    recovered: int
    active: int


#######################################
# CurrentUSModel
#######################################
class CurrentUSModel(BaseModel):
    Province_State: str
    Confirmed: int
    Deaths: int
    Recovered: int
    Active: int

#######################################
# ConfirmedModel
#######################################
class ConfirmedModel(CurrentModel): ### Changes made right here - ConfirmedModel now inherits confirmed value from CurrentModel
    confirmed: int


#######################################
# DeathsModel
#######################################
class DeathsModel(CurrentModel):   ### Changes made right here - DeathsModel now inherits deaths value from CurrentModel
    deaths: int


#######################################
# RecoveredModel
#######################################
class RecoveredModel(CurrentModel):    ### Changes made right here - RecoveredModel now inherits recovered values from CurrentModel
    recovered: int


#######################################
# ActiveModel
#######################################
class ActiveModel(CurrentModel):      ### Changes made right here - ActiveModel now inherits recovered values from CurrentModel
    active: int


#######################################
# CountryModel
#######################################
class CountryModel(CurrentModel):      ### Changes made right here - ActiveModel now inherits recovered values from CurrentModel
    location: str
    confirmed: int
    deaths: int
    recovered: int
    active: int





#######################################
# TotalModel
#######################################
class TotalModel(CurrentModel):       ### Changes made here - TotalModel can inherit values from GetCurrent and use them as part of the aggregation
    confirmed: int
    deaths: int
    recovered: int
    active: int




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
