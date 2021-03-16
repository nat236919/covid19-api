"""
FILE: get_data_US.py
DESCRIPTION: Read raw files from GitHub
AUTHOR: Elim Lemango
DATE: 16-March-2021
"""
 # Import libraries
import csv
import datetime
from typing import Dict

import pandas as pd

from .file_paths import JHU_CSSE_FILE_PATHS
from .get_data_ import data
from .helper import (helper_df_cleaning, helper_df_cols_cleaning,
                     helper_get_latest_data_url)


class data_US:
    # Get data from daily reports (USA)

    def __init__(self) -> None:
        """ Get data from helper -> the source data """
        list_of_dataframes = data()
        self.df_confirmed = list_of_dataframes['confirmed']
        self.df_deaths = list_of_dataframes['deaths']
        self.df_recovered = list_of_dataframes['recovered']

        list_of_time_series = data.get_data(time_series=True)
        self.df_time_series_confirmed = list_of_time_series['confirmed']
        self.df_time_series_deaths = list_of_time_series['deaths']
        self.df_time_series_recovered = list_of_time_series['recovered']

        self.datetime_raw = self.df_confirmed['datetime'].unique().tolist()[0]
        self.timestamp = datetime.strptime(self.datetime_raw, '%m/%d/%y').timestamp()

  def get_data_daily_reports_us() -> pd.DataFrame:
    """ Get data from BASE_URL_DAILY_REPORTS """
    # Check the latest file
    latest_base_url = helper_get_latest_data_url(JHU_CSSE_FILE_PATHS['BASE_URL_DAILY_REPORTS_US'])

    # Extract the data
    df = pd.read_csv(latest_base_url)

    # Data pre-processing
    concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
    df = helper_df_cols_cleaning(df, concerned_columns, int)
    
    return df

     # Get data from time series (US)
    def get_US_time_series() -> Dict[str, pd.DataFrame]:
        """ Get the dataset of time series for USA """
    dataframes = {}

    # Iterate through categories ('confirmed', 'deaths')
    for category in JHU_CSSE_FILE_PATHS['CATEGORIES'][:-1]:
        url = JHU_CSSE_FILE_PATHS['BASE_URL_US_TIME_SERIES'].format(category)
        
        # Extract data
        df = pd.read_csv(url)
        df = helper_df_cleaning(df)
        concerned_columns = ['Lat', 'Long_']
        df = helper_df_cols_cleaning(df, concerned_columns, float)
        dataframes[category] = df

    return dataframes