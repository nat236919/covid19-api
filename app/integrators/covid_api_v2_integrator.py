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

import pandas as pd

from models.base_model import ResponseModel
from utils.get_data import (DailyReports, DataTimeSeries,
                              get_data_lookup_table)

from models.covid_api_v2_model_aggegator import CurrentModelRoot, TimeseriesModelRoot


class CovidAPIv2Integrator:
    """ Covid-19 API v2 methods
        SCHEMA: {
            "data": Any,
            "dt": str = "{datetime}",
            "ts": int = "{timestamp}
        }
    """
    
    def __init__(self,  daily_reports: DailyReports, time_series: DataTimeSeries) -> None:
        """ Initiate instances """
        self.lookup_table = get_data_lookup_table()
        self.scheme = {
            'data': None,
            'dt': None,
            'ts': None
        }
        self.daily_reports = daily_reports
        self.time_series = time_series

        self.current_model_root = CurrentModelRoot(daily_reports)
        self.timeseries_model_root = TimeseriesModelRoot(time_series)

    #######################################################################################
    # GET - Current
    #######################################################################################
    def get_current(self) -> dict:
        """ Current data from all locations (Lastest date) """
        return self.current_model_root.get_all_countries()
    
    #######################################################################################
    # GET - Current US
    #######################################################################################
    def get_current_US(self) -> dict:
        """ Get current data for USA's situation """
        return self.current_model_root.get_us()
    
    #######################################################################################
    # GET - Country
    #######################################################################################
    def get_country(self, country_name: str) -> dict:
        """ Get a country data from its name or ISO 2 """
        return self.current_model_root.get_country(country_name)
    
    #######################################################################################
    # GET - Confirm
    #######################################################################################
    def get_confirmed(self) -> dict:
        """ Summation of all confirmed cases """
        return self.current_model_root.get_confirmed()

    #######################################################################################
    # GET - Deaths
    #######################################################################################
    def get_deaths(self) -> dict:
        return self.current_model_root.get_deaths()
    
    #######################################################################################
    # GET - Recovered
    #######################################################################################
    def get_recovered(self) -> dict:
        """ Summation of all recovers """
        return self.current_model_root.get_recovered()
    
    #######################################################################################
    # GET - Active
    #######################################################################################
    def get_active(self) -> dict:
        """ Summation of all actives """
        return self.current_model_root.get_active()
    
    #######################################################################################
    # GET - Total
    #######################################################################################
    def get_total(self) -> dict:
        """ Summation of Confirmed, Deaths, Recovered, Active """
        return self.current_model_root.get_total()
    
    #######################################################################################
    # GET - Timeseries
    #######################################################################################
    def get_time_series(self, case: str) -> dict:
        """ Get time series data from a given case
            1.) global
            2.) confirmed, deaths, recovered
        """
        return self.timeseries_model_root.get_time_series(case)

    #######################################################################################
    # GET - Timeseries US
    #######################################################################################
    def get_US_time_series(self, case: str) -> dict:
        """ Get USA time series """
        return self.timeseries_model_root.get_US_time_series(case)