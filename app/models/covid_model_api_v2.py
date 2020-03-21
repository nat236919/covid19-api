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
from utils.helper import get_data_api_v2


# Novel Corona API v2
class NovelCoronaAPIv2:
    """ Covid-19 API v2 model and its methods
        SCHEMA: {
            "data": List = {List[Any]},
            "dt": str = "{datetime}",
            "ts": int = "{timestamp}
        }
    """
    def __init__(self):
        self.list_of_dataframes = get_data_api_v2()
        self.df_confirmed = self.list_of_dataframes['confirmed']
        self.df_deaths = self.list_of_dataframes['deaths']
        self.df_recovered = self.list_of_dataframes['recovered']
        self.datetime_raw = self.df_confirmed['datetime'].unique().tolist()[0]
        self.timestamp = datetime.strptime(self.datetime_raw, '%m/%d/%y').timestamp()

    def get_current(self) -> List[Dict]:
        """ Current data (Lastest date) """
        # Create a template
        countries = self.df_confirmed['Country/Region'].unique().tolist()
        current_data = {country: {'confirmed': 0, 'deaths': 0, 'recovered': 0} for country in countries}

        # Extractor
        def extractor(col: str, df: pd.DataFrame) -> None:
            temp_data = df.T.to_dict()
            for data in temp_data.values():
                current_data[data['Country/Region']][col] += int(data[col.capitalize()])
            return None

        # Add data to current_data
        df_list = {'confirmed': self.df_confirmed, 'deaths': self.df_deaths, 'recovered': self.df_recovered}
        [extractor(col, df) for col, df in df_list.items()]

        # Sort by Confirmed
        current_data = {country_name: country_data for country_name, country_data
                                                    in sorted(current_data.items(), key=lambda data: data[-1]['confirmed'], reverse=True)}

        # Create a list
        data = []
        for k, v in current_data.items():
            data.append({
                'location': k,
                'confirmed': v['confirmed'],
                'deaths': v['deaths'],
                'recovered': v['recovered']
            })
        return data
    
    def get_confirmed(self) -> Dict[str, int]:
        """ Summation of all confirmed cases """
        data = {'confirmed': sum([int(i) for i in self.df_confirmed['Confirmed']])}
        return data
    
    def get_deaths(self) -> Dict[str, int]:
        """ Summation of all deaths """
        data = {'deaths': sum([int(i) for i in self.df_deaths['Deaths']])}
        return data
    
    def get_recovered(self) -> Dict[str, int]:
        """ Summation of all recovers """
        data = {'recovered': sum([int(i) for i in self.df_recovered['Recovered']])}
        return data
    
    def get_total(self) -> Dict[str, Any]:
        """ Summation of Confirmed, Deaths, Recovered """
        data = {
            'confirmed': self.get_confirmed()['confirmed'],
            'deaths': self.get_deaths()['deaths'],
            'recovered': self.get_recovered()['recovered']
            }
        return data
