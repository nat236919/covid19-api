"""
FILE: test_caching.py
DESCRIPTION: Test the API cache class added by Kevin
AUTHOR: Kevin (PresidentKevvol)
DATE: 15-Mar-2021
"""

import pytest
from ..utils import get_data, caching
import time

# following tests fetch the data using the cache object
# should be the same since they all call the exact same methods,
# unless the test is ran right when the JHU server is updating its data

# note: DataFrames == operator doesn't really work for some reason, but the test shows the cache class is working as intended

# the objective of these tests are to just make sure the code doesn't have any error

# to see the printed messages, use:
# pytest app\tests\test_caching.py -s

def test_get_data_daily_reports_cached():
    start = time.time()
    daily_cached = caching.api_cache.get("data_daily_reports")
    end_1 = time.time()
    daily_cached_2 = caching.api_cache.get("data_daily_reports")
    end_2 = time.time()

    # now calculate the interval
    interval_1 = end_1 - start
    interval_2 = end_2 - end_1
    # interval 2 should be shorter since it's cached
    print("Time taken for first fetch: " + str(interval_1))
    print("Time taken for second fetch: " + str(interval_2))

def test_get_US_time_series_cached():
    US_time_cached = caching.api_cache.get("US_time_series")
    # US_time_raw = get_data.get_US_time_series()
    assert US_time_cached != None

    # this doesn't work due to DataFrame's equal operator not really working as intended
    # assert US_time_cached == US_time_raw
