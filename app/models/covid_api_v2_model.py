"""
FILE: covid_api_v2_model.py
DESCRIPTION: Models for API v2
AUTHOR: Nuttaphat Arunoprayoch
DATE: 01-March-2021
"""
# Import libraries
from typing import List

from pydantic import BaseModel
from abc import ABCMeta, abstractstaticmethod

class IModel(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def get_data():
        ""T"The Model Interace"""

class CurrentModel(IModel):
    location: str
    confirmed: int
    deaths: int
    recovered: int
    active: int


    def get_data(self):
        return {self.location, self.confirmed, self.deaths, self.recovered, self.active}


#######################################
# CurrentUSModel
#######################################
class CurrentUSModel(IModel):
    Province_State: str
    Confirmed: int
    Deaths: int
    Recovered: int
    Active: int

    def get_data(self):
        return {self.Province_State, self.Confirmed, self.Deaths, self.Recovered, self.Active}


#######################################
# TotalModel
#######################################
class TotalModel(IModel):
    confirmed: int
    deaths: int
    recovered: int
    active: int

   def get_data(self):
        return {self.confirmed, self.deaths, self.recovered, self.active}


#######################################
# ConfirmedModel
#######################################
class ConfirmedModel(IModel):
    confirmed: int

    def get_data(self):
        return self.confirmed


#######################################
# DeathsModel
#######################################
class DeathsModel(IModel):
    deaths: int

    def get_data(self):
        return self.deaths

#######################################
# RecoveredModel
#######################################
class RecoveredModel(IModel):
    recovered: int

    def get_data(self):
        return self.recovered


#######################################
# ActiveModel
#######################################
class ActiveModel(IModel):
    active: int
    def get_data(self):
        return self.active


#######################################
# CountryModel
#######################################
class CountryModel(IModel):
    location: str
    confirmed: int
    deaths: int
    recovered: int
    active: int

    def get_data(self):
        return {self.location, self.confirmed, self.deaths, self.recovered, self.active}

#######################################
# TimeseriesGlobalModel
#######################################
class TimeseriesGlobalModel(IModel):
    confirmed: int
    deaths: int
    recovered: int

    def get_data(self):
        return {self.confirmed, self.deaths, self.recovered}


#######################################
# TimeseriesCaseModel
#######################################
class TimeseriesCaseCoordinatesModel(IModel):
    Lat: float
    Long: float

    def get_data(self):
        return {self.Lat, self.Long}


class TimeseriesCaseDataModel(IModel):
    date: str
    value: int

    def get_data(self):
        return {self.date, self.value}

class TimeseriesCaseModel(IModel):
    Province_State: str
    Country_Region: str
    Coordinates: TimeseriesCaseCoordinatesModel
    TimeSeries: List[TimeseriesCaseDataModel]

    def get_data(self):
        return {self.Province_State, self.Country_Region, self.Coordinates, self.TimeSeries}


#######################################
# TimeseriesUSModel
#######################################
class TimeseriesUSInfoModel(IModel):
    UID: str
    iso2: str
    iso3: str
    code3: str
    FIPS: str
    Admin2: str

    def get_data(self):
        return {self.UID, self.iso2, self.iso3, self.code3, self.FIPS, self.Admin2}


class TimeseriesUSCoordinatesModel(IModel):
    Lat: float
    Long: float

     def get_data(self):
            return {self.Lat, self.Long}

class TimeseriesUSDataModel(IModel):
    date: str
    value: int

    def get_data(self):
        return {self.date, self.value}

class TimeseriesUSModel(IModel):
    Province_State: str
    Country_Region: str
    Info: TimeseriesUSInfoModel
    Coordinates: TimeseriesUSCoordinatesModel
    TimeSeries: List[TimeseriesUSDataModel]

    def get_data(self):
        return {self.Province_State, self.Country_Region, self.Info, self.Coordinates, self.TimeSeries}


class ModelFactory():

    @staticmethod
    def get_model(modeltype):
        try:
            if modeltype == "CurrentModel":
                return CurrentModel
            if modeltype == "CurrentUSModel":
                return CurrentUSModel
            if modeltype == "TotalModel":
                return TotalModel
            if modeltype == "ConfiremedModel":
                return ConfiremedModel
            if modeltype == "DeathModel":
                return DeathModel
            if modeltype == "recoveredModel":
                return recoveredModel
            if modeltype == "ActiveModel":
                return ActiveModel
            if modeltype == "CountrytModel":
                return CountrytModel
            if modeltype == "TimeseriesGlobalModel":
                return TimeseriesGlobalModel
            if modeltype == "TimeseriesCaseCoordinatesModel":
                return TimeseriesCaseCoordinatesModel
            if modeltype == "TimeseriesCaseDataModel":
                return TimeseriesCaseDataModel
            if modeltype == "TimeseriesCaseModel":
                return TimeseriesCaseModel
            if modeltype == "TimeseriesUSInfoModel":
                return TimeseriesUSInfoModel
            if modeltype == "TimeseriesUSCoordinatesModel":
                return TimeseriesUSCoordinatesModel
            if modeltype == "TimeseriesUSDataModel":
                return TimeseriesUSDataModel
            if modeltype == "TimeseriesUSModel":
                return TimeseriesUSModel
            raise AssertionError("Model not found")
        except AssertionError as _e:
            print(_e)
            
            
