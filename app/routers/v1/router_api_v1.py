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
from utils.helper import SingletonHelper
from . import v1

sHelper = SingletonHelper.getInstance()

# Reload Integrator (APIv1)
def reload_api_v1_integrator(func):
    """ Reload a model for each quest """
    @wraps(func)
    def wrapper(*args, **kwargs):
        global COVID_API_V1, dt, ts
        COVID_API_V1 = CovidAPIv1()
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
    data = COVID_API_V1.get_current_status(list_required=True)
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
    raw_data = COVID_API_V1.get_current_status() # Get all current data
    try:
        if country_name.lower() not in ['us', 'uk'] and len(country_name) in [2]:
            country_name = sHelper.helper_lookup_country(country_name)
            data = {k: v for k, v in raw_data.items() if country_name.lower() in k.lower()}
        else:
            data = {k: v for k, v in raw_data.items() if country_name.lower() == k.lower()}

        # Add dt and ts
        data['dt'] = raw_data['dt']
        data['ts'] = raw_data['ts']

    except:
        raise HTTPException(status_code=404, detail="Item not found")

    return data


@v1.get('/timeseries/{case}')
@reload_api_v1_integrator
def timeseries(case: str) -> Dict[str, Any]:
    """ Get the time series based on a given case: confirmed, deaths, recovered """
    raw_data = COVID_API_V1.get_time_series()
    case = case.lower()

    if case in ['confirmed', 'deaths', 'recovered']:
        data = {case: raw_data[case]}
        data['dt'] = raw_data['dt']
        data['ts'] = raw_data['ts']

    else:
        raise HTTPException(status_code=404, detail="Item not found")

    return data