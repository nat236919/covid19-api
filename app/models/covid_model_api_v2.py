"""
FILE: covid_model_api_v2.py
DESCRIPTION: Covid-19 Model for API v2
AUTHOR: Nuttaphat Arunoprayoch
DATE: 14-March-2020
"""
# Import libraries
import pandas as pd
from datetime import datetime
from typing import Dict, List, Any
from utils.helper import get_data_daily_reports


class NovelCoronaAPIv2:
    """ Covid-19 API v2 model and its methods
        SCHEMA: {
            "data": Any,
            "dt": str = "{datetime}",
            "ts": int = "{timestamp}
        }
    """
    def __init__(self) -> None:
        """ Initiate DataFrame """
        self.df = get_data_daily_reports()
        concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
        self.df_grp_by_country = self.df.groupby('Country_Region')[concerned_columns].sum()
        self.df_grp_by_country[concerned_columns] = self.df_grp_by_country[concerned_columns].astype(int)
        self.datetime = max(self.df['Last_Update'].tolist())
        self.timestamp = datetime.strptime(self.datetime, '%Y-%m-%d %H:%M:%S').timestamp()
        self.scheme = {
            'data': None,
            'datetime': self.datetime,
            'timestamp': self.timestamp
        }
    
    def get_current(self) -> Dict[str, Any]:
        """ Current data from all locations (Lastest date) """
        df_grp_by_country = self.df_grp_by_country.sort_values(by='Confirmed', ascending=False)
        df_grp_by_country = df_grp_by_country.reset_index()
        df_grp_by_country.columns = ['location', 'confirmed', 'deaths', 'recovered', 'active']
        data = [v for v in df_grp_by_country.to_dict('index').values()]
        packed_data = self.scheme
        packed_data['data'] = data

        return packed_data
    
    def get_confirmed(self) -> Dict[str, Any]:
        """ Summation of all confirmed cases """
        data = self.df['Confirmed'].sum()
        packed_data = self.scheme
        packed_data['data'] = int(data)

        return packed_data

    def get_deaths(self) -> Dict[str, Any]:
        """ Summation of all deaths """
        data = self.df['Deaths'].sum()
        packed_data = self.scheme
        packed_data['data'] = int(data)

        return packed_data
    
    def get_recovered(self) -> Dict[str, Any]:
        """ Summation of all recovers """
        data = self.df['Recovered'].sum()
        packed_data = self.scheme
        packed_data['data'] = int(data)

        return packed_data

    def get_active(self) -> Dict[str, Any]:
        """ Summation of all actives """
        data = self.df['Active'].sum()
        packed_data = self.scheme
        packed_data['data'] = int(data)

        return packed_data
    
    def get_total(self) -> Dict[str, Any]:
        """ Summation of Confirmed, Deaths, Recovered, Active """
        packed_data = self.scheme
        packed_data['data'] = {
            'confirmed': int(self.df['Confirmed'].sum()),
            'deaths': int(self.df['Deaths'].sum()),
            'recovered': int(self.df['Recovered'].sum()),
            'active': int(self.df['Active'].sum())
        }
        
        return packed_data
