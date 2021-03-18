"""
FILE: file_paths.py
DESCRIPTION: Keep file paths from the data source
AUTHOR: Nuttaphat Arunoprayoch
DATE: 17-April-2020
"""

import requests
from datetime import datetime, timedelta

class JHUCSSEDatasetURL:
    # Johns Hopkins CSSE - Datasets (https://github.com/CSSEGISandData/COVID-19)
    JHU_CSSE_BASE_PATH = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/'
    JHU_CSSE_DAILY_REPORT_PATH = JHU_CSSE_BASE_PATH + 'csse_covid_19_daily_reports/'
    JHU_CSSE_DAILY_REPORT_US_PATH = JHU_CSSE_BASE_PATH + 'csse_covid_19_daily_reports_us/'
    JHU_CSSE_TIME_SERIES_PATH = JHU_CSSE_BASE_PATH + 'csse_covid_19_time_series/'
    JHU_CSSE_LOOKUP_TABLE_PATH = JHU_CSSE_BASE_PATH + 'UID_ISO_FIPS_LookUp_Table.csv'
    JHU_CSSE_CATEGORIES = ['confirmed', 'deaths', 'recovered']

    @classmethod
    def get_lookup_table_url(cls) -> None:
        return cls.JHU_CSSE_LOOKUP_TABLE_PATH
    
    @classmethod
    def get_daily_report_url(cls) -> None:
        return cls._get_latest_data_url(cls.JHU_CSSE_DAILY_REPORT_PATH + '{}.csv')
    
    @classmethod
    def get_daily_report_us_url(cls) -> None:
        return cls._get_latest_data_url(cls.JHU_CSSE_DAILY_REPORT_US_PATH + '{}.csv')
    
    @classmethod
    def get_time_series_url(cls, category: str) -> None:
        return cls.JHU_CSSE_TIME_SERIES_PATH + f'time_series_covid19_{category}_global.csv'
    
    @classmethod
    def get_time_series_us_url(cls, category: str) -> None:
        return cls.JHU_CSSE_TIME_SERIES_PATH + f'time_series_covid19_{category}_US.csv'
    
    # Get latest data
    @staticmethod
    def _get_latest_data_url(base_url: str) -> str:
        """ Get the latest base URL """
        time_format = '%m-%d-%Y'
        current_datetime = datetime.utcnow().strftime(time_format)
        latest_base_url = base_url.format(current_datetime)

        # Check the latest file by re-acquiring file
        # If not found, continue
        time_delta = 1
        while requests.get(latest_base_url).status_code == 404:
            current_datetime = datetime.strftime(datetime.utcnow() - timedelta(time_delta), time_format)
            latest_base_url = base_url.format(current_datetime)
            time_delta += 1

        return latest_base_url
