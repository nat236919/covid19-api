"""
FILE: country.py
DESCRIPTION: Countries for API v2
AUTHOR:
DATE: 14-April-2021
"""

from models.covid_api_v2.model.py import Model


class Country:
    def __init__(self, Model):
        self.model = Model

    def get_country_name(self):
        pass

    def get_current(self):
        pass

    def get_time_series(self):
        pass


class UnitedStates(Country):
    def __init__(self, Model):
        super().__init__(Model)

    def get_country_name(self):
        pass

    def get_current(self):
        pass

    def get_time_series(self):
        pass
