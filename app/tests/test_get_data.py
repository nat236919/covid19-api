"""
FILE: test_get_data.py
DESCRIPTION: Test reading raw files from GitHub
AUTHOR: Nuttaphat Arunoprayoch
DATE: 11-April-2020
"""
# Import libraries
import pandas as pd

from ..utils.get_data import (DailyReports, DataTimeSeries, get_data,
                              get_data_lookup_table)
from ..utils.time_series_interface import IDataTimeSeries
from ..utils.daily_report_interface import IDailyReports
from ..utils.daily_reports_adapter import DailyReportsAdapter

daily_reports = DailyReports()
time_series = DailyReportsAdapter()


# Test - Get Lookup table
def test_get_data_lookup_table() -> None:
    result = get_data_lookup_table()
    assert len(result) > 0
    assert isinstance(result, dict) is True


# Test - Get data from daily reports
def test_get_data_daily_reports() -> None:
    result = daily_reports.get_data_daily_reports()
    assert len(result) > 0
    assert isinstance(result, pd.DataFrame) is True 


# Test - Get data from daily reports (US)
def test_get_data_daily_reports_US() -> None:
    result = daily_reports.get_data_daily_reports(US=True)
    assert len(result) > 0
    assert isinstance(result, pd.DataFrame) is True 


# Test - Get data from time series
def test_get_data_time_series() -> None:
    result = time_series.get_data_time_series()
    assert len(result) > 0
    assert isinstance(result, dict) is True


# Test - Get data from time series (US)
def test_get_US_time_series() -> None:
    result = time_series.get_data_time_series(US=True)
    assert len(result) > 0
    assert isinstance(result, dict) is True


# Test - Get Data (API v1)
def test_get_data() -> None:
    result = get_data()
    assert len(result) > 0
    assert isinstance(result, dict) is True


# Test - Get Data (API v1)
def test_get_data(time_series = True) -> None:
    result = get_data()
    assert len(result) > 0
    assert isinstance(result, dict) is True
