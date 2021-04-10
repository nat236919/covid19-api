"""
FILE: covid_api_v2_integrator.py
DESCRIPTION: Integrators for API v2
AUTHOR: Nuttaphat Arunoprayoch
DATE: 01-March-2021
"""
# Import libraries
from datetime import datetime
from functools import wraps
from typing import Any, Dict, List
from abc import ABCMeta, abstractmethod

import pandas as pd

from pydantic import BaseModel
from models.base_model import ResponseModel
from models.covid_api_v2_model import (ActiveModel, ConfirmedModel,
                                         CountryModel, DeathsModel,
                                         RecoveredModel, TotalModel)
from utils.get_data import (DailyReports)

class ICovidAPIv2Case(metaclass=ABCMeta):
    "CovidAPIV2 Case Interface"
    
    @staticmethod
    @abstractmethod 
    def __init__(self,  daily_reports: DailyReports) -> None:
        """ Initiate instances """
    
    @staticmethod
    @abstractmethod
    def get_data(self) -> BaseModel:
        """ Summation of all confirmed cases """
    

class CovidAPIv2ConfirmedCase(ICovidAPIv2Case):
    """ Covid-19 API v2 Case
        SCHEMA: {
            "data": Any,
            "dt": str = "{datetime}",
            "ts": int = "{timestamp}
        }
    """
    
    def __init__(self,  daily_reports: DailyReports) -> None:
        """ Initiate instances """
        self.scheme = {
            'data': None,
            'dt': None,
            'ts': None
        }
        self.daily_reports = daily_reports

    #######################################################################################
    # GET - Confirm
    #######################################################################################
    @wrap_data
    def get_data(self) -> ConfirmedModel:
        """ Summation of all confirmed cases """

        self.df = self.daily_reports.get_data_daily_reports() # Get base data
        data = ConfirmedModel(
            confirmed=int(self.df['Confirmed'].sum())
        )
        return data
        
class CovidAPIv2DeathsCase(ICovidAPIv2Case):
    """ Covid-19 API v2 Case
        SCHEMA: {
            "data": Any,
            "dt": str = "{datetime}",
            "ts": int = "{timestamp}
        }
    """
    
    def __init__(self,  daily_reports: DailyReports) -> None:
        """ Initiate instances """
        self.scheme = {
            'data': None,
            'dt': None,
            'ts': None
        }
        self.daily_reports = daily_reports
    #######################################################################################
    # GET - Deaths
    #######################################################################################
    @wrap_data
    def get_data(self) -> DeathsModel:
        """ Summation of all deaths """

        self.df = self.daily_reports.get_data_daily_reports() # Get base data
        data = DeathsModel(
            deaths=int(self.df['Deaths'].sum())
        )
        return data
    
class CovidAPIv2RecoveredCase(ICovidAPIv2Case):
    """ Covid-19 API v2 Case
        SCHEMA: {
            "data": Any,
            "dt": str = "{datetime}",
            "ts": int = "{timestamp}
        }
    """
    
    def __init__(self,  daily_reports: DailyReports) -> None:
        """ Initiate instances """
        self.scheme = {
            'data': None,
            'dt': None,
            'ts': None
        }
        self.daily_reports = daily_reports
    #######################################################################################
    # GET - Recovered
    #######################################################################################
    @wrap_data
    def get_data(self) -> RecoveredModel:
        """ Summation of all recovers """

        self.df = self.daily_reports.get_data_daily_reports() # Get base data
        data = RecoveredModel(
            recovered=int(self.df['Recovered'].sum())
        )
        return data
    
class CovidAPIv2ActiveCase(ICovidAPIv2Case):
    """ Covid-19 API v2 Case
        SCHEMA: {
            "data": Any,
            "dt": str = "{datetime}",
            "ts": int = "{timestamp}
        }
    """
    
    def __init__(self,  daily_reports: DailyReports) -> None:
        """ Initiate instances """
        self.scheme = {
            'data': None,
            'dt': None,
            'ts': None
        }
        self.daily_reports = daily_reports
    #######################################################################################
    # GET - Active
    #######################################################################################
    @wrap_data
    def get_data(self) -> ActiveModel:
        """ Summation of all actives """

        self.df = self.daily_reports.get_data_daily_reports() # Get base data
        data = ActiveModel(
            active=int(self.df['Active'].sum())
        )
        return data
    
class CovidAPIv2TotalCase(ICovidAPIv2Case):
    """ Covid-19 API v2 Case
        SCHEMA: {
            "data": Any,
            "dt": str = "{datetime}",
            "ts": int = "{timestamp}
        }
    """
    def __init__(self,  daily_reports: DailyReports) -> None:
        """ Initiate instances """
        self.scheme = {
            'data': None,
            'dt': None,
            'ts': None
        }
        self.daily_reports = daily_reports    
    #######################################################################################
    # GET - Total
    #######################################################################################
    @wrap_data
    def get_data(self) -> TotalModel:
        """ Summation of Confirmed, Deaths, Recovered, Active """

        self.df = self.daily_reports.get_data_daily_reports() # Get base data
        data = TotalModel(
            confirmed=int(self.df['Confirmed'].sum()),
            deaths=int(self.df['Deaths'].sum()),
            recovered=int(self.df['Recovered'].sum()),
            active=int(self.df['Active'].sum())
        )
        return data
        
""" Wrap a result in a schemed data """
def wrap_data(func) -> ResponseModel:

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        packed_data = self.scheme
        packed_data['data'] = []
        try:
            packed_data['data'] = func(self, *args, **kwargs)
        except Exception as e:
            print(e)
        finally:
            time_format = '%m-%d-%Y'
            packed_data['dt'] = datetime.utcnow().strftime(time_format)
            packed_data['ts'] = datetime.strptime(packed_data['dt'], time_format).timestamp()
            reponse_model = ResponseModel(**packed_data)
        return reponse_model
    return wrapper