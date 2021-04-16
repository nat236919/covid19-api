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


class Total(IBuilder):

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