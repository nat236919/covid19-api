"""
FILE: concrete_helper.py
DESCRIPTION: All functions for helping small tasks
AUTHOR: Nuttaphat Arunoprayoch
DATE: 04-April-2020
"""
# Import libraries
from datetime import datetime, timedelta
from typing import List, TypeVar
from .file_paths import JHU_CSSE_FILE_PATHS

import pandas as pd

from .daily_reports_interface import IDailyReports
from .helper import Helpers

class HelpersAdapter(IDailyReports):

    def __init__(self, helper: Helpers) -> None:
        self.helper = helper
        self.latest_base_url = helper.helper_get_latest_data_url(JHU_CSSE_FILE_PATHS['BASE_URL_DAILY_REPORTS'])
        self.latest_base_US_url = helper.helper_get_latest_data_url(JHU_CSSE_FILE_PATHS['BASE_URL_DAILY_REPORTS_US'])

    # Get data from daily reports
    def get_data_daily_reports(self, US: bool = False) -> pd.DataFrame:
        """ Get data from BASE_URL_DAILY_REPORTS """
        # Extract the data
        df = pd.read_csv(self.latest_base_US_url) if US else pd.read_csv(self.latest_base_url)

        # Data pre-processing
        concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
        df = self.helper.helper_df_cols_cleaning(df, concerned_columns, int)
        
        return df
