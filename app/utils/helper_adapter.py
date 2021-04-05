"""
FILE: concrete_helper.py
DESCRIPTION: All functions for helping small tasks
AUTHOR: Nuttaphat Arunoprayoch
DATE: 04-April-2020
"""
# Import libraries
from datetime import datetime, timedelta
from typing import List, TypeVar

import pandas as pd

from .ihelper import IHelper
from .daily_reports_interface import IDailyReports

class HelperAdapter(IHelper):

    def __init__(self, IDailyReports IDailyReports) -> None:
        self.daily_reports = iDailyReport

    # Data preprocessing (DataFrame's columns)
    var_types = TypeVar('ensure_dtype', int, float, str)
    def helper_df_cols_cleaning(df: pd.DataFrame, cols: List[str], ensure_dtype: var_types = None) -> pd.DataFrame:
        """ Clean certain colomns in a DataFrame """
        df = self.daily_reports.helper_df_cols_cleaning(df, cols, ensure_dtype)

        return df

    # Get latest data
    def helper_get_latest_data_url(base_url: str) -> str:
        """ Get the latest base URL """
        latest_base_url = self.daily_reports.helper_get_latest_data_url(current_datetime)

        return latest_base_url

