"""
FILE: countryData.py
DESCRIPTION: Countries Data for API v1
AUTHOR:
DATE: 15-April-2021
"""

from models import covid_api_v2_model

class Country:
    def __init__(self, Model):
        self.model = Model

    def get_country_name(self):
        pass

    def get_current(self):
        pass

    def get_time_series(self):
        pass


class Canada(Country):
    def __init__(self, Model):
        super().__init__(Model)

    def get_country_name(self):
        pass

    def get_current(self):
        pass

    def get_time_series(self):
        pass