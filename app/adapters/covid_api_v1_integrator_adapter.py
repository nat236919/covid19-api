"""
FILE: covid_api_v1_integrator_adapter.py
DESCRIPTION: Adapter for Integrators for API v1
AUTHOR: Jerry CHen
DATE: 11-April-2021
"""

from integrators.covid_api_v1_integrator import CovidAPIv1
from utils.helper import helper_lookup_country

class ItemNotFoundException(Exception):
    pass

class CovidAPIv1Adapter:
    def __init__(self, covid_v1_api_integrator: CovidAPIv1):
        self.covid_v1_api = covid_v1_api_integrator

    def get_currrent_status_list(self):
        return self.covid_v1_api.get_current_status(list_required=True)

    def get_current_status_by_country(self, country_name: str):
        raw_data = self.covid_v1_api.get_current_status() # Get all current data
        if country_name.lower() not in ['us', 'uk'] and len(country_name) in [2]:
            country_name = helper_lookup_country(country_name)
            data = {k: v for k, v in raw_data.items() if country_name.lower() in k.lower()}
        else:
            data = {k: v for k, v in raw_data.items() if country_name.lower() == k.lower()}

        # Add dt and ts
        data['dt'] = raw_data['dt']
        data['ts'] = raw_data['ts']

        return data
        
    def get_formatted_timeseries(self, case: str):
        raw_data = self.covid_v1_api.get_time_series()
        case = case.lower()

        if case in ['confirmed', 'deaths', 'recovered']:
            data = {case: raw_data[case]}
            data['dt'] = raw_data['dt']
            data['ts'] = raw_data['ts']
        else:
            raise ItemNotFoundException()

        return data
