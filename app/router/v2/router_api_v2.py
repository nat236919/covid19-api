"""
FILE: router_api_v2.py
DESCRIPTION: all routes for API v2
AUTHOR: Nuttaphat Arunoprayoch
DATE: 04-April-2020
"""
from functools import wraps
from datetime import datetime
from typing import Dict, Any
from fastapi import HTTPException, BackgroundTasks
from starlette.requests import Request

from . import v2
from models.covid_model_api_v2 import CovidAPIv2


# Reload model (APIv2)
def reload_model_api_v2(func):
    """ Reload a model APIv2 for each quest """
    @wraps(func)
    def wrapper(*args, **kwargs):
        global covid_api_v2
        covid_api_v2 = CovidAPIv2()
        return func(*args, **kwargs)
    return wrapper


# Logging
def write_log(requested_path: str, client_ip: str) -> None:
    file_name = datetime.now().strftime('%d-%b-%Y')
    with open('logs/{}.txt'.format(file_name), mode='a+') as log_file:
        date_time_message = datetime.now().strftime('%d-%b-%Y, %H:%M:%S | ')
        message = date_time_message + requested_path + ' | ' + client_ip + '\n'
        log_file.write(message)
    return None


@v2.get('/current')
@reload_model_api_v2
def get_current(request: Request, background_tasks: BackgroundTasks) -> Dict[str, Any]:
    try:
        background_tasks.add_task(write_log, requested_path=str(request.url), client_ip=str(request.client))
        data = covid_api_v2.get_current()

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return data


@v2.get('/current/US')
@reload_model_api_v2
def get_current(request: Request, background_tasks: BackgroundTasks) -> Dict[str, Any]:
    try:
        background_tasks.add_task(write_log, requested_path=str(request.url), client_ip=str(request.client))
        data = covid_api_v2.get_current_US()

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return data


@v2.get('/total')
@reload_model_api_v2
def get_total(request: Request, background_tasks: BackgroundTasks) -> Dict[str, Any]:
    try:
        background_tasks.add_task(write_log, requested_path=str(request.url), client_ip=str(request.client))
        data = covid_api_v2.get_total()

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return data


@v2.get('/confirmed')
@reload_model_api_v2
def get_confirmed(request: Request, background_tasks: BackgroundTasks) -> Dict[str, int]:
    try:
        background_tasks.add_task(write_log, requested_path=str(request.url), client_ip=str(request.client))
        data = covid_api_v2.get_confirmed()

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return data


@v2.get('/deaths')
@reload_model_api_v2
def get_deaths(request: Request, background_tasks: BackgroundTasks) -> Dict[str, int]:
    try:
        background_tasks.add_task(write_log, requested_path=str(request.url), client_ip=str(request.client))
        data = covid_api_v2.get_deaths()

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return data


@v2.get('/recovered')
@reload_model_api_v2
def get_recovered(request: Request, background_tasks: BackgroundTasks) -> Dict[str, int]:
    try:
        background_tasks.add_task(write_log, requested_path=str(request.url), client_ip=str(request.client))
        data = covid_api_v2.get_recovered()

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return data


@v2.get('/active')
@reload_model_api_v2
def get_active(request: Request, background_tasks: BackgroundTasks) -> Dict[str, int]:
    try:
        background_tasks.add_task(write_log, requested_path=str(request.url), client_ip=str(request.client))
        data = covid_api_v2.get_active()

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return data


@v2.get('/country/{country_name}')
@reload_model_api_v2
def get_country(country_name: str, request: Request, background_tasks: BackgroundTasks) -> Dict[str, Any]:
    """ Search by name or ISO (alpha2) """
    try:
        background_tasks.add_task(write_log, requested_path=str(request.url), client_ip=str(request.client))
        raw_data = covid_api_v2.get_country(country_name.lower())

    except Exception as e:
        raise HTTPException(status_code=404, detail="Item not found")

    return raw_data


@v2.get('/timeseries/{case}')
@reload_model_api_v2
def get_time_series(case: str, request: Request, background_tasks: BackgroundTasks) -> Dict[str, Any]:
    """ Get the time series based on a given case: global, confirmed, deaths, *recovered
        * recovered will be deprecated by the source data soon
    """
    background_tasks.add_task(write_log, requested_path=str(request.url), client_ip=str(request.client))

    if case.lower() not in ['global', 'confirmed', 'deaths', 'recovered']:
            raise HTTPException(status_code=404, detail="Item not found")

    data = covid_api_v2.get_time_series(case.lower())

    return data


@v2.get('/timeseries/US/{case}')
@reload_model_api_v2
def get_US_time_series(case: str, request: Request, background_tasks: BackgroundTasks) -> Dict[str, Any]:
    """ Get the USA time series based on a given case: confirmed, deaths """
    background_tasks.add_task(write_log, requested_path=str(request.url), client_ip=str(request.client))

    if case.lower() not in ['confirmed', 'deaths']:
            raise HTTPException(status_code=404, detail="Item not found")

    data = covid_api_v2.get_US_time_series(case.lower())

    return data
