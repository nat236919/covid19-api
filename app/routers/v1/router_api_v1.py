"""
FILE: router_api_v1.py
DESCRIPTION: all routes for API v1
AUTHOR: Nuttaphat Arunoprayoch
DATE: 04-April-2020
"""
# Import libraries
from functools import wraps
from typing import Any, Dict

from fastapi import HTTPException

from integrators.covid_api_v1_integrator import CovidAPIv1
from adapters.covid_api_v1_integrator_adapter import CovidAPIv1Adapter
from . import v1


# Reload Integrator (APIv1)
def reload_api_v1_integrator(func):
    """ Reload a model for each quest """
    @wraps(func)
    def wrapper(*args, **kwargs):
        global COVID_API_V1, COVID_API_V1_ADAPTER, dt, ts
        COVID_API_V1 = CovidAPIv1()
        COVID_API_V1_ADAPTER = CovidAPIv1Adapter(COVID_API_V1)
        dt, ts = COVID_API_V1.datetime_raw, COVID_API_V1.timestamp
        return func(*args, **kwargs)
    return wrapper


@v1.get('/current')
@reload_api_v1_integrator
def current_status() -> Dict[str, int]:
    data = COVID_API_V1.get_current_status()
    return data


@v1.get('/current_list')
@reload_api_v1_integrator
def current_status_list() -> Dict[str, Any]:
    """ Coutries are kept in a List """
    data = COVID_API_V1_ADAPTER.get_currrent_status_list()
    return data


@v1.get('/total')
@reload_api_v1_integrator
def total() -> Dict[str, Any]:
    data = COVID_API_V1.get_total()
    return data


@v1.get('/confirmed')
@reload_api_v1_integrator
def confirmed_cases() -> Dict[str, int]:
    data = COVID_API_V1.get_confirmed_cases()
    return data


@v1.get('/deaths')
@reload_api_v1_integrator
def deaths() -> Dict[str, int]:
    data = COVID_API_V1.get_deaths()
    return data


@v1.get('/recovered')
@reload_api_v1_integrator
def recovered() -> Dict[str, int]:
    data = COVID_API_V1.get_recovered()
    return data


@v1.get('/countries')
@reload_api_v1_integrator
def affected_countries() -> Dict[int, str]:
    data = COVID_API_V1.get_affected_countries()
    return data


@v1.get('/country/{country_name}')
@reload_api_v1_integrator
def country(country_name: str) -> Dict[str, Any]:
    """ Search by name or ISO (alpha2) """
    try:
        data = COVID_API_V1_ADAPTER.get_current_status_by_country(country_name)
    except:
        raise HTTPException(status_code=404, detail="Item not found")
        
    return data


@v1.get('/timeseries/{case}')
@reload_api_v1_integrator
def timeseries(case: str) -> Dict[str, Any]:
    """ Get the time series based on a given case: confirmed, deaths, recovered """
    try:
        data = COVID_API_V1_ADAPTER.get_formatted_timeseries(case)
    except:
        raise HTTPException(status_code=404, detail="Item not found")

    return data
