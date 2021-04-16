"""
FILE: Current.py
DESCRIPTION: Concrete builder for getting Current Status
"""
from app.builders.v2_builder_interface import IBuilder
from app.utils.get_data import *
from abc import ABCMeta, abstractmethod
from typing import Any, Dict, List
from app.models.covid_api_v1_model import *
from app.models.covid_api_v2_model import *
# Import libraries
from datetime import datetime
from functools import wraps
from typing import Any, Dict, List
from abc import ABCMeta, abstractmethod
from app.utils.get_data import (DailyReports, DataTimeSeries,
                              get_data_lookup_table)
import pandas as pd

from app.models.base_model import ResponseModel


class Current(IBuilder):
    def get_data(self) -> List[CurrentModel]:
        """ Current data from all locations (Lastest date) """
        concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
        self.df = self.daily_reports.get_data_daily_reports()# Get base data
        self.df_grp_by_country = self.df.groupby('Country_Region')[concerned_columns].sum()
        self.df_grp_by_country[concerned_columns] = self.df_grp_by_country[concerned_columns].astype(int)

        df_grp_by_country = self.df_grp_by_country.sort_values(by='Confirmed', ascending=False)
        df_grp_by_country = df_grp_by_country.reset_index()
        df_grp_by_country.columns = ['location', 'confirmed', 'deaths', 'recovered', 'active']

        data = [CurrentModel(**v) for v in df_grp_by_country.to_dict('index').values()]

        return data
