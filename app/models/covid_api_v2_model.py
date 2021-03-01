"""
FILE: covid_api_v2_model.py
DESCRIPTION: Models for API v2
AUTHOR: Nuttaphat Arunoprayoch
DATE: 01-March-2021
"""
# Import libraries
from pydantic import BaseModel


#######################################
# CurrentModel
#######################################
class CurrentModel(BaseModel):
    location: str
    confirmed: int
    deaths: int
    recovered: int
    active: int


#######################################
# CurrentUSModel
#######################################
class CurrentUSModel(BaseModel):
    Province_State: str
    Confirmed: int
    Deaths: int
    Recovered: int
    Active: int


#######################################
# TotalModel
#######################################
class TotalModel(BaseModel):
    confirmed: int
    deaths: int
    recovered: int
    active: int


#######################################
# ConfirmedModel
#######################################
class ConfirmedModel(BaseModel):
    confirmed: int


#######################################
# DeathsModel
#######################################
class DeathsModel(BaseModel):
    deaths: int


#######################################
# RecoveredModel
#######################################
class RecoveredModel(BaseModel):
    recovered: int


#######################################
# ActiveModel
#######################################
class ActiveModel(BaseModel):
    active: int


#######################################
# CountryModel
#######################################
class CountryModel(BaseModel):
    location: str
    confirmed: int
    deaths: int
    recovered: int
    active: int


#######################################
# TimeseriesGlobalModel
#######################################
class TimeseriesGlobalModel(BaseModel):
    key: str
    confirmed: int
    deaths: int
    recovered: int
