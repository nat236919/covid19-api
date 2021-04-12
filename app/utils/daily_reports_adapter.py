# Import libraries
import csv
from typing import Dict

import pandas as pd

from .file_paths import JHU_CSSE_FILE_PATHS
from .helper import (helper_df_cleaning, helper_df_cols_cleaning,
                     helper_get_latest_data_url)
from .time_series_interface import IDataTimeSeries
from .daily_report import DailyReports

class DailyReportsAdapter(IDataTimeSeries):
    def __init__(self):
        self.report = DailyReports()


    def get_data_time_series(self, US: bool = False) -> Dict[str, pd.DataFrame]:
        dataframes = {}

        # Determine categories and url
        if US:
            categories = JHU_CSSE_FILE_PATHS['CATEGORIES'][:-1] # Select only 'confirmed' and 'deaths'
            url = JHU_CSSE_FILE_PATHS['BASE_URL_US_TIME_SERIES']
        else:
            categories = JHU_CSSE_FILE_PATHS['CATEGORIES']
            url = JHU_CSSE_FILE_PATHS['BASE_URL_TIME_SERIES']

        # Iterate through all files
        for category in categories:
            url = url.format(category)
            # Extract data from URL
            df = pd.read_csv(url)
            df = self._clean_timeseries_dataframe(df, US)
            dataframes[category] = df

        return dataframes
    
    def _clean_timeseries_dataframe(self, df: pd.DataFrame, US: bool = False) -> pd.DataFrame:
        df_cleaned = helper_df_cleaning(df)
        if US:
            df_cleaned = helper_df_cols_cleaning(df_cleaned, ['Lat', 'Long_'], float)
        return df_cleaned
