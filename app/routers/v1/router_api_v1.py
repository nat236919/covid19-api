"""
FILE: router_api_v1.py
DESCRIPTION: all routes for API v1
AUTHOR: Nuttaphat Arunoprayoch
DATE: 04-April-2020
"""
# Import libraries
from typing import Any, Dict

from fastapi import HTTPException
from app.utils.helper import helper_lookup_country
from . import v1
from app.integrators.Adapter import Adapter


@v1.get('/current')
def current_status() -> Dict[str, int]:
    data = Adapter.current_status(current_status, 1)
    return data


@v1.get('/current_list')
def current_status_list() -> Dict[str, Any]:
    """ Coutries are kept in a List """
    data = Adapter.current_status(current_status, 1)(list_required=True)
    return data


@v1.get('/total')
def total() -> Dict[str, Any]:
    data = Adapter.total(total, 1)
    return data


@v1.get('/confirmed')
def confirmed_cases() -> Dict[str, int]:
    data = Adapter.confirmed_cases(confirmed_cases, 1)
    return data


@v1.get('/deaths')
def deaths() -> Dict[str, int]:
    data = Adapter.deaths(deaths, 1)
    return data


@v1.get('/recovered')
def recovered() -> Dict[str, int]:
    data = Adapter.recovered(recovered, 1)
    return data


@v1.get('/countries')
def affected_countries() -> Dict[int, str]:
    data = Adapter.affected_countries(affected_countries, 1)
    return data


@v1.get('/country/{country_name}')
def country(country_name: str) -> Dict[str, Any]:
    """ Search by name or ISO (alpha2) """
    raw_data = Adapter.current_status(current_status, 1)
    try:
        if country_name.lower() not in ['us', 'uk'] and len(country_name) in [2]:
            country_name = helper_lookup_country(country_name)
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
def timeseries(case: str) -> Dict[str, Any]:
    """ Get the time series based on a given case: confirmed, deaths, recovered """
    raw_data = Adapter.time_series(timeseries, 1)
    case = case.lower()

    if case in ['confirmed', 'deaths', 'recovered']:
        data = {case: raw_data[case]}
        data['dt'] = raw_data['dt']
        data['ts'] = raw_data['ts']

    else:
        raise HTTPException(status_code=404, detail="Item not found")

    return data
