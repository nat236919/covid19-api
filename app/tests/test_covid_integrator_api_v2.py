"""
FILE: test_covid_model_api_v2.py
DESCRIPTION: Test Covid-19 Model for API v2
AUTHOR: Nuttaphat Arunoprayoch
DATE: 12-April-2020
"""
# Import libraries
import pytest
import pandas as pd

from ..models.covid_api_v2_model import (ActiveModel, ConfirmedModel,
                                         CountryModel, CurrentModel,
                                         CurrentUSModel, DeathsModel,
                                         RecoveredModel,
                                         TimeseriesCaseCoordinatesModel,
                                         TimeseriesCaseDataModel,
                                         TimeseriesCaseModel,
                                         TimeseriesGlobalModel,
                                         TimeseriesUSCoordinatesModel,
                                         TimeseriesUSDataModel,
                                         TimeseriesUSInfoModel,
                                         TimeseriesUSModel, TotalModel)
from ..utils.get_data import (DailyReports, DataTimeSeries,
                              get_data_lookup_table)
from ..integrators.covid_api_v2_integrator import CovidAPIv2Integrator


# Prepare the model
DAILY_REPORTS = DailyReports()
DATA_TIME_SERIES = DataTimeSeries()
COVID_API_V2 = CovidAPIv2Integrator(DAILY_REPORTS, DATA_TIME_SERIES)


# Test Initial attibutes
def test_init() -> None:
    assert isinstance(COVID_API_V2.lookup_table, dict) is True
    assert isinstance(COVID_API_V2.scheme, dict) is True
    assert isinstance(
        COVID_API_V2.daily_reports.get_data_daily_reports(), pd.DataFrame) is True
    assert isinstance(
        COVID_API_V2.time_series.get_data_time_series(), dict) is True


# Test - Get Current
def test_get_current() -> None:
    result = COVID_API_V2.get_current().data
    assert isinstance(result, list) is True
    assert isinstance(result[0], CurrentModel) is True
    assert isinstance(result[0].location, str) is True
    assert isinstance(result[0].confirmed, int) is True
    assert isinstance(result[0].deaths, int) is True
    assert isinstance(result[0].recovered, int) is True
    assert isinstance(result[0].active, int) is True


# Test - Get country
def test_get_country() -> None:
    result_th = COVID_API_V2.get_country('th').data
    assert isinstance(result_th, CountryModel) is True
    assert result_th.location == 'Thailand'

    result_cn = COVID_API_V2.get_country('china').data
    assert isinstance(result_cn, CountryModel) is True
    assert result_cn.location == 'China'


# Test - Get Confirmed
def test_get_confirmed() -> None:
    result = COVID_API_V2.get_confirmed().data
    assert isinstance(result, ConfirmedModel) is True
    assert isinstance(result.confirmed, int) is True


# Test - Get Deaths
def test_get_deaths() -> None:
    result = COVID_API_V2.get_deaths().data
    assert isinstance(result, DeathsModel) is True
    assert isinstance(result.deaths, int) is True


# Test - Get Recovered
def test_get_recovered() -> None:
    result = COVID_API_V2.get_recovered().data
    assert isinstance(result, RecoveredModel) is True
    assert isinstance(result.recovered, int) is True


# Test - Get Active
def test_get_active() -> None:
    result = COVID_API_V2.get_active().data
    assert isinstance(result, ActiveModel) is True
    assert isinstance(result.active, int) is True


# Test - Get Total
def test_get_total() -> None:
    result = COVID_API_V2.get_total().data
    assert isinstance(result, TotalModel) is True
    assert isinstance(result.confirmed, int) is True
    assert isinstance(result.deaths, int) is True
    assert isinstance(result.recovered, int) is True
    assert isinstance(result.active, int) is True


# Test - Get Time Series
def test_get_time_series() -> None:
    result = COVID_API_V2.get_time_series('global').data
    assert isinstance(result, list) is True

    result = COVID_API_V2.get_time_series('confirmed').data
    assert isinstance(result[0], TimeseriesCaseModel) is True
    assert isinstance(result[0].Province_State, str) is True
    assert isinstance(result[0].Country_Region, str) is True
    assert isinstance(result[0].Coordinates,
                      TimeseriesCaseCoordinatesModel) is True
    assert isinstance(result[0].TimeSeries, list) is True

    result = COVID_API_V2.get_time_series('deaths').data
    assert isinstance(result[0], TimeseriesCaseModel) is True
    assert isinstance(result[0].Province_State, str) is True
    assert isinstance(result[0].Country_Region, str) is True
    assert isinstance(result[0].Coordinates,
                      TimeseriesCaseCoordinatesModel) is True
    assert isinstance(result[0].TimeSeries, list) is True

    result = COVID_API_V2.get_time_series('recovered').data
    assert isinstance(result[0], TimeseriesCaseModel) is True
    assert isinstance(result[0].Province_State, str) is True
    assert isinstance(result[0].Country_Region, str) is True
    assert isinstance(result[0].Coordinates,
                      TimeseriesCaseCoordinatesModel) is True
    assert isinstance(result[0].TimeSeries, list) is True


# Test - Get Time Series (US)
@pytest.mark.skip(reason='Time consuming since US timeseries API requires heavy calc')
def test_get_US_time_series() -> None:
    result = COVID_API_V2.get_US_time_series('confirmed').data
    assert isinstance(result[0], TimeseriesUSModel) is True
    assert isinstance(result[0].Province_State, str) is True
    assert isinstance(result[0].Country_Region, str) is True
    assert isinstance(result[0].Info, TimeseriesUSInfoModel) is True
    assert isinstance(result[0].Coordinates,
                      TimeseriesUSCoordinatesModel) is True
    assert isinstance(result[0].TimeSeries, list) is True

    result = COVID_API_V2.get_US_time_series('deaths').data
    assert isinstance(result[0], TimeseriesUSModel) is True
    assert isinstance(result[0].Province_State, str) is True
    assert isinstance(result[0].Country_Region, str) is True
    assert isinstance(result[0].Info, TimeseriesUSInfoModel) is True
    assert isinstance(result[0].Coordinates,
                      TimeseriesUSCoordinatesModel) is True
    assert isinstance(result[0].TimeSeries, list) is True
