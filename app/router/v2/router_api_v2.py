"""
FILE: router_api_v2.py
DESCRIPTION: all routes for API v2
AUTHOR: Nuttaphat Arunoprayoch
DATE: 04-April-2020
"""
from functools import wraps
from typing import Dict, Any

from . import v2
from utils.helper import lookup_country
from models.covid_model_api_v2 import NovelCoronaAPIv2


# Reload model (APIv2)
def reload_model_api_v2(func):
    """ Reload a model APIv2 for each quest """
    @wraps(func)
    def wrapper(*args, **kwargs):
        global novel_corona_api_v2
        novel_corona_api_v2 = NovelCoronaAPIv2()
        return func(*args, **kwargs)
    return wrapper


@v2.get('/current')
@reload_model_api_v2
def get_current() -> Dict[str, Any]:
    try:
        data = novel_corona_api_v2.get_current()

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return data


@v2.get('/total')
@reload_model_api_v2
def get_total() -> Dict[str, Any]:
    try:
        data = novel_corona_api_v2.get_total()

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return data


@v2.get('/confirmed')
@reload_model_api_v2
def get_confirmed() -> Dict[str, int]:
    try:
        data = novel_corona_api_v2.get_confirmed()

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return data


@v2.get('/deaths')
@reload_model_api_v2
def get_deaths() -> Dict[str, int]:
    try:
        data = novel_corona_api_v2.get_deaths()

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return data


@v2.get('/recovered')
@reload_model_api_v2
def get_recovered() -> Dict[str, int]:
    try:
        data = novel_corona_api_v2.get_recovered()

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return data


@v2.get('/active')
@reload_model_api_v2
def get_active() -> Dict[str, int]:
    try:
        data = novel_corona_api_v2.get_active()

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return data


@v2.get('/country/{country_name}')
@reload_model_api_v2
def get_country(country_name: str) -> Dict[str, Any]:
    """ Search by name or ISO (alpha2) """
    raw_data = novel_corona_api_v2.get_current() # Get all current data
    try:
        if country_name.lower() not in ['us', 'uk'] and len(country_name) in [2]:
            country_name = lookup_country(country_name)
            data = [i for i in raw_data['data'] if country_name.lower() in i.get("location").lower()]
        else:
            data = [i for i in raw_data['data'] if country_name.lower() == i.get("location").lower()]
        
        raw_data['data'] = data[0]

    except:
        raise HTTPException(status_code=404, detail="Item not found")

    return raw_data


@v2.get('/timeseries/{case}')
@reload_model_api_v2
def get_time_series(case: str) -> Dict[str, Any]:
    """ Get the time series based on a given case: global, confirmed, deaths, *recovered
        * recovered will be deprecated by the source data soon
    """
    if case.lower() not in ['global', 'confirmed', 'deaths', 'recovered']:
            raise HTTPException(status_code=404, detail="Item not found")

    data = novel_corona_api_v2.get_time_series(case.lower())

    return data
