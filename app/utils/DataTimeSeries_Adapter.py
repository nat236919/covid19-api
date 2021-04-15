"""
FILE: DataTimeSeries_Adapter.py
DESCRIPTION: Provides DataTimeSeries objects with an adapter when using methods in class helper.py
AUTHOR: Faizan Rabbi
DATE: 15-April-2021
"""
# Import libraries
from datetime import datetime, timedelta
from typing import List, TypeVar

import pandas as pd

from .helper import Helper
from .Helper_Interface import HelperInterface

class DataTimeSeriesAdapter(HelperInterface):

    def __init__(self, timeSeries) -> None:
        self.DataTimeSeries = timeSeries

    var_types = TypeVar('ensure_dtype', int, float, str)

    def helper_df_cleaning(df: pd.DataFrame) -> pd.DataFrame:
        return self.DataTimeSeries.helper_df_cleaning('')
        """ Fill all empty values with am empty string (e.g., '') """

    def helper_df_cols_cleaning(df: pd.DataFrame, cols: List[str], ensure_dtype: var_types = None) -> pd.DataFrame:
        return self.DataTimeSeries.helper_df_cols_cleaning(df,cols,ensure_dtype)
        """ Clean certain columns in a DataFrame """
