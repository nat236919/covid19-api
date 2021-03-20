"""
FILE: covid_api_v2_model.py
DESCRIPTION: Models for API v2
AUTHOR: Nuttaphat Arunoprayoch
DATE: 01-March-2021
"""
# Import libraries
from typing import List, Optional

from pydantic import BaseModel


#######################################
# CurrentModel
#######################################
class CurrentModel(BaseModel):
    location: str
    confirmed: int
    deaths: int
    recovered: int
    active: int


#######################################
# CurrentUSModel
#######################################
class CurrentUSModel(BaseModel):
    province_state: str
    confirmed: int
    deaths: int
    recovered: int
    active: int


#######################################
# CountryModel
#######################################
class CurrentCountryModel(BaseModel):
    location: str
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


class TimeseriesUSInfoModel(BaseModel):
    UID: str
    iso2: str
    iso3: str
    code3: str
    FIPS: str
    Admin2: str


class TimeseriesCaseModel(BaseModel):
    Province_State: str
    Country_Region: str
    Coordinates: TimeseriesCaseCoordinatesModel
    Info: Optional[TimeseriesUSInfoModel]
    TimeSeries: List[TimeseriesCaseDataModel]
