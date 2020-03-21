"""
PROJECT: Covid2019-API
DESCRIPTION: Daily level information on various cases
AUTHOR: Nuttaphat Arunoprayoch
DATE: 9-Feb-2020
RUN SERVER: uvicorn main:app --reload
"""
# Import libraries
import sys
import pycountry
from functools import wraps
from typing import Dict, Any

from fastapi import FastAPI, HTTPException
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from api.covid_model import NovelCoronaAPI
from api_v2.covid_model_api_v2 import NovelCoronaAPIv2

# Setup variables
version = f"{sys.version_info.major}.{sys.version_info.minor}"
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Reload model
def reload_model(func):
    """ Reload a model for each quest """
    @wraps(func)
    def wrapper(*args, **kwargs):
        global novel_corona_api, dt, ts
        novel_corona_api = NovelCoronaAPI()
        dt, ts = novel_corona_api.datetime_raw, novel_corona_api.timestamp
        return func(*args, **kwargs)
    return wrapper


# Reload model (APIv2)
def reload_model_api_v2(func):
    """ Reload a model APIv2 for each quest """
    @wraps(func)
    def wrapper(*args, **kwargs):
        global novel_corona_api_v2, dt_v2, ts_v2
        novel_corona_api_v2 = NovelCoronaAPIv2()
        dt_v2, ts_v2 = novel_corona_api_v2.datetime_raw, novel_corona_api_v2.timestamp
        return func(*args, **kwargs)
    return wrapper


# Add datetime and timestamp
def add_dt_and_ts(func):
    """ Add datetime and timestamp to APIv2 """
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        data['dt'] = dt_v2
        data['ts'] = ts_v2
        return data
    return wrapper


# Look up a country name from a country code
def lookup_country(country):
    """ Look up a country name from a country code """
    country_name = pycountry.countries.lookup(country).name # Select the first portion of str when , is found
    if ',' in country_name:
        country_name = country_name.split(',')[0]
    elif ' ' in country_name:
        country_name = country_name.split(' ')[-1]
    return country_name


"""
SECTION: Default routes
DESCRIPTION: Routes to the landing page and APi documentation
"""
# Landing page
@app.get('/')
def read_root(request: Request):
    """ Landing page """
    return templates.TemplateResponse('index.html', {"request": request})


# API documentation
@app.get('/docs')
def read_docs() -> None:
    """ API documentation """
    return RedirectResponse(url='/docs')


"""
SECTION: API v2
DESCRIPTION: New API (v2)
DATE: 14-March-2020
"""
@app.get('/v2/current', tags=['v2'])
@reload_model_api_v2
@add_dt_and_ts
def current() -> Dict[str, Any]:
    try:
        data = novel_corona_api_v2.get_current()
        response = {"data": data}

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return response


@app.get('/v2/total', tags=['v2'])
@reload_model_api_v2
@add_dt_and_ts
def get_total() -> Dict[str, Any]:
    try:
        data = novel_corona_api_v2.get_total()
        response = {"data": data}

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return response


@app.get('/v2/confirmed', tags=['v2'])
@reload_model_api_v2
@add_dt_and_ts
def get_confirmed() -> Dict[str, int]:
    try:
        data = novel_corona_api_v2.get_confirmed()
        response = {"data": data['confirmed']}

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return response


@app.get('/v2/deaths', tags=['v2'])
@reload_model_api_v2
@add_dt_and_ts
def get_deaths() -> Dict[str, int]:
    try:
        data = novel_corona_api_v2.get_deaths()
        response = {"data": data['deaths']}

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return response


@app.get('/v2/recovered', tags=['v2'])
@reload_model_api_v2
@add_dt_and_ts
def get_recovered() -> Dict[str, int]:
    try:
        data = novel_corona_api_v2.get_recovered()
        response = {"data": data['recovered']}

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    return response

@app.get('/v2/country/{country_name}', tags=['v2'])
@reload_model_api_v2
@add_dt_and_ts
def country(country_name: str) -> Dict[str, Any]:
    """ Search by name or ISO (alpha2) """
    raw_data = novel_corona_api_v2.get_current() # Get all current data
    try:
        if country_name.lower() not in ['us', 'uk'] and len(country_name) in [2]:
            country_name = lookup_country(country_name)
            data = [i for i in raw_data if country_name.lower() in i.get("location").lower()]
        else:
            data = [i for i in raw_data if country_name.lower() == i.get("location").lower()]
        response = {"data": data}
    except:
        raise HTTPException(status_code=404, detail="Item not found")

    return response


"""
SECTION: API v1
REMARK: No further improvement intended unless necessary
"""
@app.get('/current', tags=['v1'])
@reload_model
def current_status() -> Dict[str, int]:
    data = novel_corona_api.get_current_status()
    return data


@app.get('/current_list', tags=['v1'])
@reload_model
def current_status_list() -> Dict[str, Any]:
    """ Coutries are kept in a List """
    data = novel_corona_api.get_current_status(list_required=True)
    return data


@app.get('/total', tags=['v1'])
@reload_model
def total() -> Dict[str, Any]:
    data = novel_corona_api.get_total()
    return data


@app.get('/confirmed', tags=['v1'])
@reload_model
def confirmed_cases() -> Dict[str, int]:
    data = novel_corona_api.get_confirmed_cases()
    return data


@app.get('/deaths', tags=['v1'])
@reload_model
def deaths() -> Dict[str, int]:
    data = novel_corona_api.get_deaths()
    return data


@app.get('/recovered', tags=['v1'])
@reload_model
def recovered() -> Dict[str, int]:
    data = novel_corona_api.get_recovered()
    return data


@app.get('/countries', tags=['v1'])
@reload_model
def affected_countries() -> Dict[int, str]:
    data = novel_corona_api.get_affected_countries()
    return data


@app.get('/country/{country_name}', tags=['v1'])
@reload_model
def country(country_name: str) -> Dict[str, Any]:
    """ Search by name or ISO (alpha2) """
    raw_data = novel_corona_api.get_current_status() # Get all current data
    try:
        if country_name.lower() not in ['us', 'uk'] and len(country_name) in [2]:
            country_name = lookup_country(country_name)
            data = {k: v for k, v in raw_data.items() if country_name.lower() in k.lower()}
        else:
            data = {k: v for k, v in raw_data.items() if country_name.lower() == k.lower()}

        # Add dt and ts
        data['dt'] = raw_data['dt']
        data['ts'] = raw_data['ts']

    except:
        raise HTTPException(status_code=404, detail="Item not found")

    return data


@app.get('/timeseries/{case}', tags=['v1'])
@reload_model
def timeseries(case: str) -> Dict[str, Any]:
    """ Get the time series based on a given case: confirmed, deaths, recovered """
    raw_data = novel_corona_api.get_time_series()
    case = case.lower()

    if case in ['confirmed', 'deaths', 'recovered']:
        data = {case: raw_data[case]}
        data['dt'] = raw_data['dt']
        data['ts'] = raw_data['ts']

    else:
        raise HTTPException(status_code=404, detail="Item not found")

    return data
