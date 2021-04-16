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


class CurrentUS(IBuilder):

    def get_data(self) -> List[CurrentUSModel]:
        """ Get current data for USA's situation """
        self.df_US = self.daily_reports.get_data_daily_reports(US=True)  # Get base data

        concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
        df = self.df_US.groupby(['Province_State'])[concerned_columns].sum().sort_values(by='Confirmed',
                                                                                         ascending=False)
        df = df[concerned_columns].astype(int)
        df = df.reset_index()
        df.columns = ['Province_State'] + concerned_columns

        data = [CurrentUSModel(**v) for v in df.to_dict('index').values()]

        return data
