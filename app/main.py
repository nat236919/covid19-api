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

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from models.covid_model import NovelCoronaAPI

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
        global novel_corona_api
        novel_corona_api = NovelCoronaAPI()
        return func(*args, **kwargs)
    return wrapper


@app.get('/')
@reload_model
def read_root(request: Request):
    """ Landing page """
    data = novel_corona_api.get_total()
    return templates.TemplateResponse('index.html', {"request": request, "data": data})


@app.get('/docs')
@reload_model
def read_docs() -> None:
    """ API documentation """
    return RedirectResponse(url='/docs')


@app.get('/current')
@reload_model
def current_status() -> Dict[str, int]:
    data = novel_corona_api.get_current_status()
    return data


@app.get('/current_list')
@reload_model
def current_status_list() -> Dict[str, Any]:
    """ Coutries are kept in a List """
    raw_data = novel_corona_api.get_current_status()
    data = {
        'countries': [{k: v for k, v in raw_data.items() if k not in ['ts', 'dt']}],
        'dt': raw_data['dt'],
        'ts': raw_data['ts']
    }

    return data


@app.get('/total')
@reload_model
def total() -> Dict[str, Any]:
    data = novel_corona_api.get_total()
    return data


@app.get('/confirmed')
@reload_model
def confirmed_cases() -> Dict[str, int]:
    data = novel_corona_api.get_confirmed_cases()
    return data


@app.get('/deaths')
@reload_model
def deaths() -> Dict[str, int]:
    data = novel_corona_api.get_deaths()
    return data


@app.get('/recovered')
@reload_model
def recovered() -> Dict[str, int]:
    data = novel_corona_api.get_recovered()
    return data


@app.get('/countries')
@reload_model
def affected_countries() -> Dict[int, str]:
    data = novel_corona_api.get_affected_countries()
    return data


@app.get('/country/{country_name}')
@reload_model
def country(country_name: str) -> Dict[str, Any]:
    """ Search by name or ISO (alpha2) """
    raw_data = novel_corona_api.get_current_status() # Get all current data
    try:
        if country_name.lower() not in ['us', 'uk'] and len(country_name) in [2]:
            country_name = pycountry.countries.lookup(country_name).name # Select the first portion of str when , is found
            if ',' in country_name:
                country_name = country_name.split(',')[0]
            elif ' ' in country_name:
                country_name = country_name.split(' ')[-1]
            print(country_name)
            data = {k: v for k, v in raw_data.items() if country_name.lower() in k.lower()}
        else:
            data = {k: v for k, v in raw_data.items() if country_name.lower() == k.lower()}

        # Add dt and ts
        data['dt'] = raw_data['dt']
        data['ts'] = raw_data['ts']

    except:
        data = {}

    return data


@app.get('/timeseries/{case}')
@reload_model
def timeseries(case: str) -> Dict[str, Any]:
    """ Get the time series based on a given case: confirmed, deaths, recovered """
    raw_data = novel_corona_api.get_time_series()
    case = case.lower()
    data = {}

    if case in ['confirmed', 'deaths', 'recovered']:
        data = {
            case: raw_data[case],
            'dt': raw_data['dt'],
            'ts': raw_data['ts']
        }

    return data
