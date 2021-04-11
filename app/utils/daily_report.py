# Import libraries
import csv
from typing import Dict

import pandas as pd

from .file_paths import JHU_CSSE_FILE_PATHS
from .helper import (helper_df_cleaning, helper_df_cols_cleaning,
                     helper_get_latest_data_url)
from daily_report_interface import IDailyReports

class DailyReports(IDailyReports):
    def __init__(self) -> None: 
        self.latest_base_url = helper_get_latest_data_url(JHU_CSSE_FILE_PATHS['BASE_URL_DAILY_REPORTS'])
        self.latest_base_US_url = helper_get_latest_data_url(JHU_CSSE_FILE_PATHS['BASE_URL_DAILY_REPORTS_US'])

    # Get data from daily reports
    def get_data_daily_reports(self, US: bool = False) -> pd.DataFrame:
        """ Get data from BASE_URL_DAILY_REPORTS """
        # Extract the data
        df = pd.read_csv(self.latest_base_US_url) if US else pd.read_csv(self.latest_base_url)

        # Data pre-processing
        concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
        df = helper_df_cols_cleaning(df, concerned_columns, int)
        
        return df
