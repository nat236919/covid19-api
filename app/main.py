"""
PROJECT: NovelCoronaAPI
DESCRIPTION: Daily level information on various cases
AUTHOR: Nuttaphat Arunoprayoch
DATE: 9-Feb-2020
RUN SERVER: uvicorn main:app --reload
"""
# Import libraries
import sys
from fastapi import FastAPI
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from typing import Dict, Any
from model import NovelCoronaAPI

# Setup variables
version = f"{sys.version_info.major}.{sys.version_info.minor}"
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

novel_corona_api = NovelCoronaAPI()


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


@app.get('/current')
def current_status() -> Dict[str, int]:
    data = novel_corona_api.get_current_status()
    return data


@app.get('/confirmed')
def confirmed_cases() -> Dict[str, int]:
    data = novel_corona_api.get_confirmed_cases()
    return data


@app.get('/deaths')
def deaths() -> Dict[str, int]:
    data = novel_corona_api.get_deaths()
    return data


@app.get('/recovered')
def recovered() -> Dict[str, int]:
    data = novel_corona_api.get_recovered()
    return data


@app.get('/countries')
def affected_countries() -> Dict[int, str]:
    data = novel_corona_api.get_affected_countries()
    return data


@app.get('/country/{country_name}')
def country(country_name: str) -> Dict[str, Any]:
    country_name = country_name.lower().capitalize()
    raw_data = novel_corona_api.get_current_status()

    try:
        data = {country_name: raw_data[country_name]}
    except:
        data = {'result': 'Not Found'}

    return data
