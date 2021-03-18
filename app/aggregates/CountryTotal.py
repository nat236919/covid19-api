"""
FILE: CountryTotal.py
DESCRIPTION: A model component containing all confirmed cases, deaths, and recoveries
             for a specified country.
AUTHOR: Vivian Dcruze
DATE: 15-March-2021
"""

from models.covid_api_v1_model import (CountriesModel, TotalModel)

class CountryTotal:
    totalmodel: TotalModel
    countrymodel: CountriesModel
    country: str

    def __init__(self, tm: TotalModel, cm: CountriesModel, country: str) -> None:
        self.totalmodel = date
        self.countrymodel = timestamp
        self.country = country