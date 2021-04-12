"""
FILE: covid_api_v1_integrator_adapter.py
DESCRIPTION: Adapter for Integrators for API v1
AUTHOR: Jerry CHen
DATE: 11-April-2021
"""

from integrators.covid_api_v1_integrator import CovidAPIv1


class CovidAPIv1Adapter:
    def get_current_status_by_country(country_name: str):
        raw_data = COVID_API_V1.get_current_status() # Get all current data
        if country_name.lower() not in ['us', 'uk'] and len(country_name) in [2]:
            country_name = helper_lookup_country(country_name)
            data = {k: v for k, v in raw_data.items() if country_name.lower() in k.lower()}
        else:
            data = {k: v for k, v in raw_data.items() if country_name.lower() == k.lower()}

        # Add dt and ts
        data['dt'] = raw_data['dt']
        data['ts'] = raw_data['ts']

        return data
        

    def get_formatted_timeseries():
        raw_data = COVID_API_V1.get_time_series()
        case = case.lower()

        if case in ['confirmed', 'deaths', 'recovered']:
            data = {case: raw_data[case]}
            data['dt'] = raw_data['dt']
            data['ts'] = raw_data['ts']
        else:
            raise HTTPException(status_code=404, detail="Item not found")

        return data

    def get_currrent_status_list():
        return COVID_API_V1.get_current_status(list_required=True)