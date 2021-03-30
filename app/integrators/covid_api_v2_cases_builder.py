"""
FILE: covid_api_v2_cases_builder.py
DESCRIPTION: Builder of the Case for API v2
AUTHOR: Nuttaphat Arunoprayoch
DATE: 30-March-2021
"""
# Import libraries
from datetime import datetime
from functools import wraps
from typing import Any, Dict, List
from abc import ABCMeta, abstractmethod

import pandas as pd

from models.base_model import ResponseModel
from models.covid_api_v2_model import (ActiveModel, ConfirmedModel,
                                         CountryModel, CurrentModel,
                                         CurrentUSModel, DeathsModel,
                                         RecoveredModel, TotalModel)
from utils.get_data import (DailyReports, DataTimeSeries,
                              get_data_lookup_table)

from .covid_api_v2_cases_builder_interface import ICaseBuilder

class CaseBuilder(ICaseBuilder):
    "The Concrete Builder for the case entity"

    def __init__(self) -> None:
        """ Initiate instances """
        self.lookup_table = get_data_lookup_table()
        self.scheme = {
            'data': None,
            'dt': None,
            'ts': None
        }
        self.daily_reports = DailyReports()
        self.time_series = DataTimeSeries()

    def wrap_data(func) -> ResponseModel:
        """ Wrap a result in a schemed data """
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

    #######################################################################################
    # GET - Current
    #######################################################################################
    @wrap_data
    def get_current(self) -> List[CurrentModel]:
        """ Current data from all locations (Lastest date) """
        concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
        self.df = self.daily_reports.get_data_daily_reports() # Get base data
        self.df_grp_by_country = self.df.groupby('Country_Region')[concerned_columns].sum()
        self.df_grp_by_country[concerned_columns] = self.df_grp_by_country[concerned_columns].astype(int)

        df_grp_by_country = self.df_grp_by_country.sort_values(by='Confirmed', ascending=False)
        df_grp_by_country = df_grp_by_country.reset_index()
        df_grp_by_country.columns = ['location', 'confirmed', 'deaths', 'recovered', 'active']

        data = [CurrentModel(**v) for v in df_grp_by_country.to_dict('index').values()]

        return data
    
    #######################################################################################
    # GET - Current US
    #######################################################################################
    @wrap_data
    def get_current_US(self) -> List[CurrentUSModel]:
        """ Get current data for USA's situation """
        self.df_US = self.daily_reports.get_data_daily_reports(US=True) # Get base data

        concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
        df = self.df_US.groupby(['Province_State'])[concerned_columns].sum().sort_values(by='Confirmed', ascending=False)
        df = df[concerned_columns].astype(int)
        df = df.reset_index()
        df.columns = ['Province_State'] + concerned_columns

        data = [CurrentUSModel(**v) for v in df.to_dict('index').values()]

        return data
    
    #######################################################################################
    # GET - Country
    #######################################################################################
    @wrap_data
    def get_country(self, country_name: str) -> CountryModel:
        """ Get a country data from its name or ISO 2 """
        concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
        self.df = self.daily_reports.get_data_daily_reports() # Get base data
        self.df_grp_by_country = self.df.groupby('Country_Region')[concerned_columns].sum()
        self.df_grp_by_country[concerned_columns] = self.df_grp_by_country[concerned_columns].astype(int)

        df_grp_by_country = self.df_grp_by_country.sort_values(by='Confirmed', ascending=False)
        df_grp_by_country = df_grp_by_country.reset_index()
        df_grp_by_country.columns = ['location', 'confirmed', 'deaths', 'recovered', 'active']

        all_country_data = [CountryModel(**v) for v in df_grp_by_country.to_dict('index').values()]


        # Check input
        if not isinstance(country_name, str) or not country_name.isalpha():
            return {}

        # Search for a given country
        country_name = country_name.lower()
        country_name_from_code = self.lookup_table.get(country_name.upper(), '').lower()

        data = [country_data for country_data in all_country_data if country_data.location.lower() in [country_name, country_name_from_code]]
        data = data[0] if data else {}

        return data
    
    #######################################################################################
    # GET - Confirm
    #######################################################################################
    @wrap_data
    def get_confirmed(self) -> ConfirmedModel:
        """ Summation of all confirmed cases """
        self.df = self.daily_reports.get_data_daily_reports() # Get base data
        data = ConfirmedModel(
            confirmed=int(self.df['Confirmed'].sum())
        )
        return data

    #######################################################################################
    # GET - Deaths
    #######################################################################################
    @wrap_data
    def get_deaths(self) -> DeathsModel:
        """ Summation of all deaths """
        self.df = self.daily_reports.get_data_daily_reports() # Get base data
        data = DeathsModel(
            deaths=int(self.df['Deaths'].sum())
        )
        return data
    
    #######################################################################################
    # GET - Recovered
    #######################################################################################
    @wrap_data
    def get_recovered(self) -> RecoveredModel:
        """ Summation of all recovers """
        self.df = self.daily_reports.get_data_daily_reports() # Get base data
        data = RecoveredModel(
            recovered=int(self.df['Recovered'].sum())
        )
        return data
    
    #######################################################################################
    # GET - Active
    #######################################################################################
    @wrap_data
    def get_active(self) -> ActiveModel:
        """ Summation of all actives """
        self.df = self.daily_reports.get_data_daily_reports() # Get base data
        data = ActiveModel(
            active=int(self.df['Active'].sum())
        )
        return data
    
    #######################################################################################
    # GET - Total
    #######################################################################################
    @wrap_data
    def get_total(self) -> TotalModel:
        """ Summation of Confirmed, Deaths, Recovered, Active """
        self.df = self.daily_reports.get_data_daily_reports() # Get base data
        data = TotalModel(
            confirmed=int(self.df['Confirmed'].sum()),
            deaths=int(self.df['Deaths'].sum()),
            recovered=int(self.df['Recovered'].sum()),
            active=int(self.df['Active'].sum())
        )
        return data
