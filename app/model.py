"""
FILE: model.py
DESCRIPTION: Prepare the data as API-ready
AUTHOR: Nuttaphat Arunoprayoch
DATE: 9-Feb-2020
"""
# Import libraries
import pandas as pd
from datetime import datetime
from typing import Dict, List, Any
from helper import get_data


# Create a model and its methods
class NovelCoronaAPI:
    """ Model and Its methods """
    def __init__(self) -> None:
        list_of_dataframes = get_data()
        self.df_confirmed = list_of_dataframes['confirmed']
        self.df_deaths = list_of_dataframes['deaths']
        self.df_recovered = list_of_dataframes['recovered']

    def get_current_status(self) -> Dict[str, Any]:
        """ Current data (Lastest date) """
        # Create a template
        countries = self.df_confirmed['Country/Region'].unique().tolist()
        current_data = {country: {'confirmed': 0, 'deaths': 0, 'recovered': 0} for country in countries}

        # Calculate the data
        sum_confirmed = self.df_confirmed.T.to_dict()
        sum_deaths = self.df_deaths.T.to_dict()
        sum_recovered = self.df_recovered.T.to_dict()

        for data in sum_confirmed.values():
            current_data[data['Country/Region']]['confirmed'] += int(data['Confirmed'])

        for data in sum_deaths.values():
            current_data[data['Country/Region']]['deaths'] += int(data['Deaths'])

        for data in sum_recovered.values():
            current_data[data['Country/Region']]['recovered'] += int(data['Recovered'])
        
        # Add timestamp
        current_data['ts'] = datetime.timestamp(datetime.now())

        return current_data

    def get_confirmed_cases(self) -> Dict[str, int]:
        """ Summation of all confirmed cases """
        return {'confirmed': sum([int(i) for i in self.df_confirmed['Confirmed']])}

    def get_deaths(self) -> Dict[str, int]:
        """ Summation of all deaths """
        return {'deaths': sum([int(i) for i in self.df_deaths['Deaths']])}

    def get_recovered(self) -> Dict[str, int]:
        """ Summation of all recovers """
        return {'recovered': sum([int(i) for i in self.df_recovered['Recovered']])}
    
    def get_affected_countries(self) -> Dict[str, List]:
        """ The affected countries """
        countries = self.df_confirmed['Country/Region'].unique().tolist()
        return {'countries': countries}
