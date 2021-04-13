"""
FILE: test_get_data.py
DESCRIPTION: Test reading raw files from GitHub
AUTHOR: Nuttaphat Arunoprayoch
DATE: 11-April-2020
"""
# Import libraries
import pandas as pd
from ..utils import getData # Calling getData function instead of get_data method

getDataVar = getInstance.get_data() # Creating object which contains single instance of class and so we do not have to continually instantiate the class 

# Test - Get Lookup table
def test_get_data_lookup_table() -> None:
    result = getDataVar.get_data_lookup_table() 
    assert len(result) > 0
    assert isinstance(result, dict) is True


# Test - Get data from daily reports
def test_get_data_daily_reports() -> None:
    result = getDataVar.get_data_daily_reports()
    assert len(result) > 0
    assert isinstance(result, pd.DataFrame) is True 


# Test - Get data from time series
def test_get_data_time_series() -> None:
    result = getDataVar.get_data_time_series()
    assert len(result) > 0
    assert isinstance(result, dict) is True


# Test - Get data from time series (US)
def test_get_US_time_series() -> None:
    result = getDataVar.get_US_time_series()
    assert len(result) > 0
    assert isinstance(result, dict) is True


# Test - Get Data (API v1)
def test_get_data() -> None:
    result = getDataVar.get_data()
    assert len(result) > 0
    assert isinstance(result, dict) is True


# Test - Get Data (API v1)
def test_get_data(time_series = True) -> None:
    result = getDataVar.get_data()
    assert len(result) > 0
    assert isinstance(result, dict) is True
