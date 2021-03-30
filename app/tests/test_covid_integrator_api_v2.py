"""
FILE: test_covid_model_api_v2.py
DESCRIPTION: Test Covid-19 Model for API v2
AUTHOR: Nuttaphat Arunoprayoch
DATE: 12-April-2020
"""
# Import libraries
import pytest
import pandas as pd
from ..utils import get_data
from ..integrators import covid_api_v2_integrator


# Prepare the model
INTEGRATOR = covid_api_v2_integrator.CovidAPIv2Integrator()


# Test Initial attibutes
@pytest.mark.skip(reason="outdated test")
def test_init() -> None:
    assert isinstance(INTEGRATOR.df, pd.DataFrame) is True
    assert isinstance(INTEGRATOR.df_time_series, dict) is True
    assert isinstance(INTEGRATOR.df_US_time_series, dict) is True
    assert isinstance(INTEGRATOR.lookup_table, dict) is True
    assert isinstance(INTEGRATOR.df_grp_by_country, pd.DataFrame) is True
    assert isinstance(INTEGRATOR.datetime, str) is True
    assert isinstance(INTEGRATOR.timestamp, float) is True
    assert isinstance(INTEGRATOR.scheme, dict) is True


# Test - Get Current
def test_get_current() -> None:
    result = INTEGRATOR.get_current()['data']
    assert isinstance(result, list) is True
    assert isinstance(result[0], dict) is True
    assert isinstance(result[0]['location'], str) is True
    assert isinstance(result[0]['confirmed'], int) is True
    assert isinstance(result[0]['deaths'], int) is True
    assert isinstance(result[0]['recovered'], int) is True
    assert isinstance(result[0]['active'], int) is True


# Test - Get country
def test_get_country() -> None:
    result = INTEGRATOR.get_country('th')['data']
    assert isinstance(result, dict) is True
    assert result['location'] == 'Thailand'

    result = INTEGRATOR.get_country('china')['data']
    assert isinstance(result, dict) is True
    assert result['location'] == 'China'


# Test - Get Confirmed
def test_get_confirmed() -> None:
    result = INTEGRATOR.get_confirmed()
    assert isinstance(result, dict) is True
    assert isinstance(result['data'], int) is True


# Test - Get Deaths
def test_get_deaths() -> None:
    result = INTEGRATOR.get_confirmed()
    assert isinstance(result, dict) is True
    assert isinstance(result['data'], int) is True


# Test - Get Recovered
def test_get_recovered() -> None:
    result = INTEGRATOR.get_confirmed()
    assert isinstance(result, dict) is True
    assert isinstance(result['data'], int) is True


# Test - Get Active
def test_get_active() -> None:
    result = INTEGRATOR.get_confirmed()
    assert isinstance(result, dict) is True
    assert isinstance(result['data'], int) is True


# Test - Get Total
def test_get_total() -> None:
    result = INTEGRATOR.get_total()['data']
    assert isinstance(result, dict) is True
    assert isinstance(result['confirmed'], int) is True
    assert isinstance(result['deaths'], int) is True
    assert isinstance(result['recovered'], int) is True
    assert isinstance(result['active'], int) is True


# Test - Get Time Series
def test_get_time_series() -> None:
    result = INTEGRATOR.get_time_series('global')['data']
    assert isinstance(result, list) is True

    result = INTEGRATOR.get_time_series('confirmed')['data']
    assert isinstance(result, list) is True
    assert isinstance(result[0]['Province/State'], str) is True
    assert isinstance(result[0]['Country/Region'], str) is True
    assert isinstance(result[0]['Coordinates'], dict) is True
    assert isinstance(result[0]['TimeSeries'], list) is True

    result = INTEGRATOR.get_time_series('deaths')['data']
    assert isinstance(result, list) is True
    assert isinstance(result[0]['Province/State'], str) is True
    assert isinstance(result[0]['Country/Region'], str) is True
    assert isinstance(result[0]['Coordinates'], dict) is True
    assert isinstance(result[0]['TimeSeries'], list) is True

    result = INTEGRATOR.get_time_series('recovered')['data']
    assert isinstance(result, list) is True
    assert isinstance(result[0]['Province/State'], str) is True
    assert isinstance(result[0]['Country/Region'], str) is True
    assert isinstance(result[0]['Coordinates'], dict) is True
    assert isinstance(result[0]['TimeSeries'], list) is True


# Test - Get Time Series (US)
def test_get_US_time_series() -> None:
    result = INTEGRATOR.get_US_time_series('gibberish')
    assert bool(result['data']) is False

    result = INTEGRATOR.get_US_time_series('confirmed')['data']
    assert isinstance(result, list) is True
    assert isinstance(result[0]['Province_State'], str) is True
    assert isinstance(result[0]['Country_Region'], str) is True
    assert isinstance(result[0]['Info'], dict) is True
    assert isinstance(result[0]['Coordinates'], dict) is True
    assert isinstance(result[0]['TimeSeries'], list) is True

    result = INTEGRATOR.get_US_time_series('deaths')['data']
    assert isinstance(result, list) is True
    assert isinstance(result[0]['Province_State'], str) is True
    assert isinstance(result[0]['Country_Region'], str) is True
    assert isinstance(result[0]['Info'], dict) is True
    assert isinstance(result[0]['Coordinates'], dict) is True
    assert isinstance(result[0]['TimeSeries'], list) is True
