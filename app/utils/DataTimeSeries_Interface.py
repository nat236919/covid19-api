"""
FILE: DataTimeSeries_Interface
DESCRIPTION: Provides an Interface for class DataTimeSeries
AUTHOR: Faizan Rabbi
DATE: 15-April-2021
"""
# Import libraries
import csv
from typing import Dict

import pandas as pd
from abc import ABCMeta, abstractmethod

class IDataTimeSeries(metaclass=ABCMeta):

    @abstractmethod
    def get_data_time_series(self, US: bool = False) -> Dict[str, pd.DataFrame]:
        """Obtains the dataset from JHU_CSSE_FILE_PATHS"""

    @abstractmethod
    def _clean_timeseries_dataframe(self, df: pd.DataFrame, US: bool = False) -> pd.DataFrame:
        """Cleans DataFrame"""
