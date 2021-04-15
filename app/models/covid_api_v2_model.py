"""
FILE: covid_api_v2_model.py
DESCRIPTION: Models for API v2
AUTHOR: Nuttaphat Arunoprayoch
DATE: 01-March-2021
"""
# Import libraries
from typing import List

from pydantic import BaseModel


class Model:
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
    # CurrentCANModel
    #######################################
    class CurrentCANModel(BaseModel):
        Province_State: str
        Confirmed: int
        Deaths: int
        Recovered: int
        Active: int


    #######################################
    # TotalModel
    #######################################
    class TotalModel(BaseModel):
        confirmed: int
        deaths: int
        recovered: int
        active: int


    #######################################
    # ConfirmedModel
    #######################################
    class ConfirmedModel(BaseModel):
        confirmed: int


    #######################################
    # DeathsModel
    #######################################
    class DeathsModel(BaseModel):
        deaths: int


    #######################################
    # RecoveredModel
    #######################################
    class RecoveredModel(BaseModel):
        recovered: int


    #######################################
    # ActiveModel
    #######################################
    class ActiveModel(BaseModel):
        active: int


    #######################################
    # CountryModel
    #######################################
    class CountryModel(BaseModel):
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


    class TimeseriesCaseModel(BaseModel):
        Province_State: str
        Country_Region: str
        Coordinates: TimeseriesCaseCoordinatesModel
        TimeSeries: List[TimeseriesCaseDataModel]


    #######################################
    # TimeseriesCANModel
    #######################################
    class TimeseriesCANInfoModel(BaseModel):
        UID: str
        iso2: str
        iso3: str
        code3: str
        FIPS: str
        Admin2: str


    class TimeseriesCANCoordinatesModel(BaseModel):
        Lat: float
        Long: float


    class TimeseriesCANDataModel(BaseModel):
        date: str
        value: int


    class TimeseriesCANModel(BaseModel):
        Province_State: str
        Country_Region: str
        Info: BaseModel.TimeseriesCANInfoModel
        Coordinates: TimeseriesCANCoordinatesModel
        TimeSeries: List[TimeseriesCANDataModel]
