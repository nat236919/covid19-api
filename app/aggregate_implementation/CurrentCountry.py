"""
FILE: CountryModel.py
DESCRIPTION: A model component containing that aggregate TotalModel to CountryModel
AUTHOR: Ka Hei Chan
DATE: 17-March-2021
"""
from typing import *
from pydantic import BaseModel

from app.models.covid_api_v1_model import CurrentModel
from app.models.covid_api_v2_model import (CountryModel, TotalModel)
from app.utils.get_data import get_data_lookup_table, DailyReports, DataTimeSeries

class CountryTotal:
    location: str
    confirmed: int
    deaths: int
    recovered: int
    active: int

    def __init__(self, location, confirmed, deaths, recovered, active):
        self.scheme = {
            'location': None,
            'confirmed': None,
            'deaths': None,
            'recovered': None,
            'active': None
        }
    def data(self, country_name: str) -> CountryModel :
        concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
        self.df = self.daily_reports.get_data_daily_reports()  # Get base data
        self.df_grp_by_country = self.df.groupby('Country_Region')[concerned_columns].sum()
        self.df_grp_by_country[concerned_columns] = self.df_grp_by_country[concerned_columns].astype(int)

        df_grp_by_country = self.df_grp_by_country.sort_values(by='Confirmed', ascending=False)
        df_grp_by_country = df_grp_by_country.reset_index()
        df_grp_by_country.columns = ['location', 'confirmed', 'deaths', 'recovered', 'active']

        data = [CurrentModel(**v) for v in df_grp_by_country.to_dict('index').values()]
        self.country_models = data
