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
        self.coordinates = None
        # added a state field ensuring the object is properly instantiated before calling .build()
        self.state = 'started'

    def __check_state(self):
        if self.coordinates != None and self.timeseries != None and len(self.timeseries) > 0:
            self.state = 'finished'
        else:
            self.state = 'building'
    # getting state
    def get_state(self):
        return self.state

    def set_coordinates(self, lat, long):
        cord = TimeseriesCaseCoordinatesModel(Lat=lat, Long=long)
        self.coordinates = cord
        self.__check_state()

    # adds one entry to the list
    def add_time_series_entry(self, date, value):
        self.timeseries.append(TimeseriesCaseDataModel(date=date, value=value))
        self.__check_state()

    # add whole map to list
    def add_time_series(self, temp_time_series_dict):
        timeseries_data_model_list = [TimeseriesCaseDataModel(date=k, value=v) for k, v in temp_time_series_dict.items()]
        self.timeseries.extend(timeseries_data_model_list)
        self.__check_state()

    def build(self) -> TimeseriesCaseModel:
        # might add code regarding the current state of this builder
        # if self.state != 'finished':
        #       something...

        return TimeseriesCaseModel(
            Province_State=self.province_state,
            Country_Region=self.country_region,
            Coordinates=self.coordinates,
            TimeSeries=self.timeseries
        )

class TimeseriesCaseModelBuilderDirect(object):
    '''
    a builder class for TimeseriesCaseModel like above
    but this one takes in the 'data' object directly and does not require calling the methods
    in the code that uses this class
    '''
    def __init__(self, data):
        self.builder = TimeseriesCaseModelBuilder(data['Province/State'], data['Country/Region'])
        lat = float(data['Lat']) if data['Lat'] else 0
        long = float(data['Long']) if data['Long'] else 0
        self.builder.set_coordinates(lat, long)
        excluded_cols = ['Province/State', 'Country/Region', 'Lat', 'Long']
        self.builder.add_time_series({k: int(v) for k, v in data.items() if k not in excluded_cols})

    # can be called right after init
    def build(self) -> TimeseriesCaseModel:
        return self.builder.build()


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
