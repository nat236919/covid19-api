"""
FILE: test_covid_model_api_v1.py
DESCRIPTION: Test Covid-19 Model for API v1
AUTHOR: Maria Elsa
DATE: 14-October 2020
"""
# Import libraries
import pytest
import pandas as pd
from ..utils import get_data
from ..integrators import covid_api_v1_integrator


# Prepare the model
INTEGRATOR = covid_api_v1_integrator.CovidAPIv1()

# Test Initial attributes
def test_init() -> None:
    assert isinstance(INTEGRATOR.df_confirmed, pd.DataFrame) is True
    assert isinstance(INTEGRATOR.df_deaths, pd.DataFrame) is True
    assert isinstance(INTEGRATOR.df_recovered, pd.DataFrame) is True
    assert isinstance(INTEGRATOR.df_time_series_confirmed, dict) is True
    assert isinstance(INTEGRATOR.df_time_series_deaths, dict) is True
    assert isinstance(INTEGRATOR.df_time_series_recovered, dict) is True
    assert isinstance(INTEGRATOR.datetime_raw, str) is True
    assert isinstance(INTEGRATOR.timestamp, float) is True
