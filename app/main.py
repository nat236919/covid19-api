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
from typing import Dict
from model import NovelCoronaAPI

# Setup variables
version = f"{sys.version_info.major}.{sys.version_info.minor}"
app = FastAPI()
novel_corona_api = NovelCoronaAPI()


@app.get("/")
async def read_root():
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python {version}"
    return {"message": message}


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
