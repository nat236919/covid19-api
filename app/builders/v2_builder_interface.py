"""
FILE: v2_builder_interface.py
DESCRIPTION: Builder interface for builder pattern
"""
from abc import ABCMeta, abstractmethod
from typing import Any, Dict, List
from app.models.covid_api_v1_model import *
from app.models.covid_api_v2_model import *
from app.utils.get_data import (DailyReports, get_data_lookup_table,DataTimeSeries)
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


class IBuilder():
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

    @abstractmethod
    def get_data(self): pass
    "for implement function"
