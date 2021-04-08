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

class TimeseriesCaseModelBuilder(object):
    '''
    a builder class for building TimeseriesCaseModel
    that can be used in other parts of the project
    '''

    def __init__(self, province_state, country_region):
        self.province_state = province_state
        self.country_region = country_region
        self.timeseries = []

    def set_coordinates(self, lat, long):
        cord = TimeseriesCaseCoordinatesModel(Lat=lat, Long=long)
        self.coordinates = cord

    def add_time_series(self, date, value):
        self.timeseries.append(TimeseriesCaseDataModel(date=date, value=value))

    def build(self) -> TimeseriesCaseModel:
        return TimeseriesCaseModel(
            Province_State=self.province_state,
            Country_Region=self.country_region,
            Coordinates=self.coordinates,
            TimeSeries=self.timeseries
        )

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

class TimeseriesUSModelBuilder(object):
    """
    a builder class for TimeseriesUSModel that can be used in
    covid_api_v2_integrator.py : CovidAPIv2Integrator.get_US_time_series()
    to make code reading and updating easier
    """

    def __init__(self, data):
        # set the basic fields
        self.Province_State = data['Province_State']
        self.Country_Region = data['Country_Region']

        # extract all the aggregate fields
        self.set_info_model(
            UID=data['UID'],
            iso2=data['iso2'],
            iso3=data['iso3'],
            code3=data['code3'],
            FIPS=data['FIPS'],
            Admin2=data['Admin2'],
        )
        self.set_coordinates_model(
            Lat=float(data['Lat']) if data['Lat'] else 0,
            Long=float(data['Long_']) if data['Long_'] else 0
        )
        self.extract_timeseries(data)

    def set_info_model(self, UID, iso2, iso3, code3, FIPS, Admin2):
        self.info_model = TimeseriesUSInfoModel(
            UID=UID,
            iso2=iso2,
            iso3=iso3,
            code3=code3,
            FIPS=FIPS,
            Admin2=Admin2,
        )

    def set_coordinates_model(self, Lat, Long):
        self.coordinates_model = TimeseriesUSCoordinatesModel(Lat=Lat, Long=Long)

    def extract_timeseries(self, data):
        excluded_cols = ['UID', 'iso2', 'iso3', 'code3', 'FIPS',
                        'Admin2','Province_State', 'Country_Region', 'Lat', 'Long_',
                        'Combined_Key','Population']
        temp_time_series_dict = {k: int(v) for k, v in data.items() if k not in excluded_cols}
        self.timeseries_data_model_list = [TimeseriesUSDataModel(date=k, value=v) for k, v in temp_time_series_dict.items()]

    def build(self) -> TimeseriesUSModel:
        return TimeseriesUSModel(
            Province_State=self.Province_State,
            Country_Region=self.Country_Region,
            Info=self.info_model,
            Coordinates=self.coordinates_model,
            TimeSeries=self.timeseries_data_model_list
        )
