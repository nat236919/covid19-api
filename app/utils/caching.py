"""
FILE: caching.py
DESCRIPTION: Implements a cache to temporarily store data fetched from JHU
AUTHOR: Kevin (PresidentKevvol)
DATE: 12-Mar-2021
"""

import csv
from typing import Dict

import pandas as pd

from .file_paths import JHU_CSSE_FILE_PATHS
from .get_data import *
from .helper import (helper_df_cleaning, helper_df_cols_cleaning,
                     helper_get_latest_data_url)

from datetime import datetime, timedelta

"""
the expire time of the cache in minutes
default to 180 mins = 3 hours
when this much time after an initial access has passed, the cahce should reset
"""
DEFAULT_EXPIRE_TIME = 180

"""
A cache object using the aggregate design pattern
fields inside here are not visible and can only be accessed by public methods
"""
class COVID_APICache:
    cached_values: Dict[str, any]
    fetch_methods: Dict[str, any]
    expire_time_dict: Dict[str, datetime]
    expire_time: float

    def __init__(self, expire_time=DEFAULT_EXPIRE_TIME):
        self.cached_values = {}
        self.fetch_methods = {"lookup_table": get_data_lookup_table,
        "data_daily_reports": get_data_daily_reports,
        "data_daily_reports_us": get_data_daily_reports_us,
        "data_time_series": get_data_time_series,
        "US_time_series": get_US_time_series,
        "data": get_data,
        }
        self.expire_time_dict = {}
        self.expire_time = expire_time

    """
    the actual public method to get the cached values
    returns cached data if there is active cahced data
    """
    def get(self, name, *args):
        # if there is an active cache and the expiration time has not been reached
        if name in self.cached_values and name in self.expire_time_dict and datetime.now() < self.expire_time_dict[name]:
            # return the cached data
            return self.cached_values[name]
        else: # if there is a need to fetch new data
            # if the cache has not be populated at all or expire time reached
            self.__get_value_from_server(name, *args)
            # reset expiration time
            self.expire_time_dict[name] = datetime.now() + timedelta(minutes=self.expire_time)
            return self.cached_values[name]

    """
    using code from get_data.py
    fetchs a value from the JHU server and store it in the cache
    """
    def __get_value_from_server(self, name, *args):
        self.cached_values[name] = self.fetch_methods[name](*args)

    """
    setter method to change the expire time
    """
    def set_expire_time(self, time_in_minutes):
        self.expire_time = time_in_minutes

# create the instant of the object for all other code to access
# there can be multiple cache objects of course
api_cache = COVID_APICache()

# an adapter for the COVID_APICache object
# with the cache object (or rather a reference to it) inside as the adaptee
# so that the same method names can be used in any client using the get data code parts with the cache
# to minimize confusion, complexity, and the need to change code
class API_cache_adapter(object):
    cache: COVID_APICache
    def __init__(self, c):
        self.cache = c

    def get_data_lookup_table(self) -> Dict[str, str]:
        return self.cache.get("lookup_table")

    def get_data_daily_reports(self) -> pd.DataFrame:
        return self.cache.get("data_daily_reports")

    def get_data_daily_reports_us(self) -> pd.DataFrame:
        return self.cache.get("data_daily_reports_us")

    def get_data_time_series(self) -> Dict[str, pd.DataFrame]:
        return self.cache.get("data_time_series")

    def get_US_time_series(self) -> Dict[str, pd.DataFrame]:
        return self.cache.get("US_time_series")

    def get_data(time_series: bool = False) -> Dict[str, pd.DataFrame]:
        return self.cache.get("data", time_series)
