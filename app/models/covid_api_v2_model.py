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
from app.utils.get_data import get_data_daily_reports


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
# AggregatedConcernedColumns
#######################################
class AggregatedConcernedColumns:

    def __init__(self):
        self.df = get_data_daily_reports()  # Get base data

    def get_confirmed(self) -> ConfirmedModel:
        """ Summation of all confirmed cases """
        data = ConfirmedModel(
            confirmed=int(self.df['Confirmed'].sum())
        )
        return data

    def get_deaths(self) -> DeathsModel:
        """ Summation of all deaths """
        data = DeathsModel(
            deaths=int(self.df['Deaths'].sum())
        )
        return data

    def get_recovered(self) -> RecoveredModel:
        """ Summation of all recovers """
        data = RecoveredModel(
            recovered=int(self.df['Recovered'].sum())
        )
        return data

    def get_active(self) -> ActiveModel:
        """ Summation of all actives """
        data = ActiveModel(
            active=int(self.df['Active'].sum())
        )
        return data

    def get_total(self) -> TotalModel:
        """ Summation of Confirmed, Deaths, Recovered, Active """
        data = TotalModel(
            confirmed=int(self.df['Confirmed'].sum()),
            deaths=int(self.df['Deaths'].sum()),
            recovered=int(self.df['Recovered'].sum()),
            active=int(self.df['Active'].sum())
        )
        return data


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
