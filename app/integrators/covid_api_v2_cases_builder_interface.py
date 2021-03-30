"""
FILE: covid_api_v2_builder_interface.py
DESCRIPTION: Builder Interface for API v2
AUTHOR: Nuttaphat Arunoprayoch
DATE: 30-March-2021
"""
# Import libraries
from typing import Any, Dict, List
from abc import ABCMeta, abstractmethod

from models.covid_api_v2_model import (ActiveModel, ConfirmedModel,
                                         CountryModel, CurrentModel,
                                         CurrentUSModel, DeathsModel,
                                         RecoveredModel,
                                         TimeseriesCaseCoordinatesModel,
                                         TimeseriesCaseDataModel,
                                         TimeseriesCaseModel,
                                         TimeseriesGlobalModel,
                                         TimeseriesUSCoordinatesModel,
                                         TimeseriesUSDataModel,
                                         TimeseriesUSInfoModel,
                                         TimeseriesUSModel, TotalModel)                       

class ICaseBuilder(metaclass=ABCMeta):
    "The Builder Interface"

    @staticmethod
    @abstractmethod   
    def wrap_data():
        """ Wrap a result in a schemed data """

    @staticmethod
    @abstractmethod
    def get_current() -> List[CurrentModel]:
        """ Current data from all locations (Lastest date) """
    
    @staticmethod
    @abstractmethod
    def get_current_US() -> List[CurrentUSModel]:
        """ Get current data for USA's situation """

    @staticmethod
    @abstractmethod
    def get_country(country_name: str) -> CountryModel:
        """ Get a country data from its name or ISO 2 """
    
    @staticmethod
    @abstractmethod
    def get_confirmed() -> ConfirmedModel:
        """ Summation of all confirmed cases """

    @staticmethod
    @abstractmethod
    def get_deaths() -> DeathsModel:
        """ Summation of all deaths """
    
    @staticmethod
    @abstractmethod
    def get_recovered() -> RecoveredModel:
        """ Summation of all recovers """
    
    @staticmethod
    @abstractmethod
    def get_active() -> ActiveModel:
        """ Summation of all actives """

    @staticmethod
    @abstractmethod
    def get_total() -> TotalModel:
        """ Summation of Confirmed, Deaths, Recovered, Active """
