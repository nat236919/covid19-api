"""
FILE: router_api_v2.py
DESCRIPTION: all routes for API v2
AUTHOR: Nuttaphat Arunoprayoch
DATE: 04-April-2020
"""
# Import libraries
from datetime import datetime
from functools import wraps
from typing import Any, Dict

from fastapi import BackgroundTasks, HTTPException
from integrators.covid_api_v2_integrator import CovidAPIv2Integrator
from starlette.requests import Request

from . import v2

# Initiate Integrator
COVID_API_V2 = CovidAPIv2Integrator()


# Logging
def write_log(requested_path: str, client_ip: str) -> None:
    time_format = '%d-%b-%Y'
    file_name = datetime.now().strftime(time_format)
    with open('logs/{}.txt'.format(file_name), mode='a+') as log_file:
        date_time_message = datetime.now().strftime(f'{time_format}, %H:%M:%S | ')
        message = date_time_message + requested_path + ' | ' + client_ip + '\n'
        log_file.write(message)
    return None


@v2.get('/current')
async def get_current(request: Request, background_tasks: BackgroundTasks) -> Dict[str, Any]:
    """
    Get the current situation data from all reported countries

    - **location**: a country's name
    - **confirmed**: confirmed cases
    - **deaths**:  death cases
    - **recovered**: recovered cases
    - **active**: active cases
    """
    try:
        background_tasks.add_task(write_log, requested_path=str(request.url), client_ip=str(request.client))
        data = COVID_API_V2.get_current()

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return data


@v2.get('/current/US')
async def get_current_us(request: Request, background_tasks: BackgroundTasks) -> Dict[str, Any]:
    """
    Get all data from USA's current situation

    - **Province_State**: State's name
    - **Confirmed**: confirmed cases
    - **Deaths**: death cases
    - **Recovered**: recovered cases
    - **Active**: active cases
    """
    try:
        background_tasks.add_task(write_log, requested_path=str(request.url), client_ip=str(request.client))
        data = COVID_API_V2.get_current_US()

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return data


@v2.get('/total')
async def get_total(request: Request, background_tasks: BackgroundTasks) -> Dict[str, Any]:
    """
    Get the total numbers of all cases

    - **confirmed**: confirmed cases
    - **deaths**:  death cases
    - **recovered**: recovered cases
    - **active**: active cases
    """
    try:
        background_tasks.add_task(write_log, requested_path=str(request.url), client_ip=str(request.client))
        data = COVID_API_V2.get_total()

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return data


@v2.get('/confirmed')
async def get_confirmed(request: Request, background_tasks: BackgroundTasks) -> Dict[str, int]:
    """
    Get the total numbers of confirmed cases

    - **confirmed**: confirmed cases
    """
    try:
        background_tasks.add_task(write_log, requested_path=str(request.url), client_ip=str(request.client))
        data = COVID_API_V2.get_confirmed()

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return data


@v2.get('/deaths')
async def get_deaths(request: Request, background_tasks: BackgroundTasks) -> Dict[str, int]:
    """
    Get the total numbers of death cases

    - **deaths**:  death cases
    """
    try:
        background_tasks.add_task(write_log, requested_path=str(request.url), client_ip=str(request.client))
        data = COVID_API_V2.get_deaths()

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return data


@v2.get('/recovered')
async def get_recovered(request: Request, background_tasks: BackgroundTasks) -> Dict[str, int]:
    """
    Get the total numbers of recovered cases

    - **recovered**: recovered case
    """
    try:
        background_tasks.add_task(write_log, requested_path=str(request.url), client_ip=str(request.client))
        data = COVID_API_V2.get_recovered()

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return data


@v2.get('/active')
async def get_active(request: Request, background_tasks: BackgroundTasks) -> Dict[str, int]:
    """
    Get the total numbers of active cases

    - **active**: active case
    """
    try:
        background_tasks.add_task(write_log, requested_path=str(request.url), client_ip=str(request.client))
        data = COVID_API_V2.get_active()

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return data


@v2.get('/country/{country_name}')
async def get_country(country_name: str, request: Request, background_tasks: BackgroundTasks) -> Dict[str, Any]:
    """
    Get the data based on a county's name or its ISO code

    - **location**: a country's name
    - **confirmed**: confirmed cases
    - **deaths**:  death cases
    - **recovered**: recovered cases
    - **active**: active cases
    \f
    :param country_name: A country name or its ISO code (ALPHA-2)
    """
    try:
        background_tasks.add_task(write_log, requested_path=str(request.url), client_ip=str(request.client))
        raw_data = COVID_API_V2.get_country(country_name.lower())

    except Exception:
        raise HTTPException(status_code=404, detail="Item not found")

    return raw_data


@v2.get('/timeseries/{case}')
async def get_time_series(case: str, request: Request, background_tasks: BackgroundTasks) -> Dict[str, Any]:
    """
    Get the time series based on a given case: global, confirmed, deaths, recovered
    
    global
    - **key**: datetime
    - **confirmed**: confirmed cases
    - **deaths**:  death cases
    - **recovered**: recovered case

    confirmed, deaths, recovered
    - **Province_State**: State's name
    - **Country_Region**: Country's name
    - **Coordinates**: {"Lat": int, "Long": int}
    - **TimeSeries**: [{"date": datetime, "value": int}]
    \f
    param: case: string case -> global, confirmed, deaths, recovered
    """
    background_tasks.add_task(write_log, requested_path=str(request.url), client_ip=str(request.client))

    if case.lower() not in ['global', 'confirmed', 'deaths', 'recovered']:
            raise HTTPException(status_code=404, detail="Item not found")

    data = COVID_API_V2.get_time_series(case.lower())

    return data


@v2.get('/timeseries/US/{case}')
async def get_US_time_series(case: str, request: Request, background_tasks: BackgroundTasks) -> Dict[str, Any]:
    """
    Get the USA time series based on a given case:

    **confirmed**, **deaths**

    - **Province_State**: State's name
    - **Country_Region**: Country's name
    - **Info**:{
        - **UID**: UID
        - **iso2**: ISO2
        - **iso3**: ISO3
        - **code3**: CODE3
        - **FIPS**: FIPS
        - **Admin2**: Admin2
    }
    - **Coordinates**: {
        - **Lat**: float
        - **Long**: float
    }
    - **TimeSeries**: [
        - {"date: datetime, "value": int}
    ]
    \f
    param: case: string case -> confirmed, deaths
    """
    background_tasks.add_task(write_log, requested_path=str(request.url), client_ip=str(request.client))

    if case.lower() not in ['confirmed', 'deaths']:
            raise HTTPException(status_code=404, detail="Item not found")

    data = COVID_API_V2.get_US_time_series(case.lower())

    return data
