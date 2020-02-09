"""
FILE: model.py
DESCRIPTION: Prepare the data as API-ready
AUTHOR: Nuttaphat Arunoprayoch
DATE: 9-Feb-2020
"""
# Import libraries
import pandas as pd
from datetime import date
from typing import Dict, List, Any
from helper import get_data


# Data Cleaning
def data_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """ Clean and select all current data """
    df['Date'] = df['Date'].apply(pd.to_datetime)
    df.drop(['Sno'], axis=1, inplace=True)
    df['Country'].replace({'Mainland China': 'China'}, inplace=True)

    # Filter current data
    d = df['Date'][-1:].astype('str')
    year = int(d.values[0].split('-')[0])
    month = int(d.values[0].split('-')[1])
    day = int(d.values[0].split('-')[2].split()[0])
    df = df[df['Date'] > pd.Timestamp(date(year,month,day))]

    return df


# Create a model and its methods
class NovelCoronaAPI:
    """ Model and Its methods """
    def __init__(self) -> None:
        self.df = data_cleaning(get_data())

    def get_current_status(self) -> Dict[str, Any]:
        """ Current data (Lastest date) """
        df_grp = self.df.groupby('Country')['Confirmed', 'Deaths', 'Recovered'].sum()
        data = df_grp.T.to_dict()
        return data

    def get_confirmed_cases(self) -> Dict[str, int]:
        """ Summation of all confirmed cases """
        return {'confirmed': int(self.df['Confirmed'].sum())}

    def get_deaths(self) -> Dict[str, int]:
        """ Summation of all deaths """
        return {'deaths': int(self.df['Deaths'].sum())}

    def get_recovered(self) -> Dict[str, int]:
        """ Summation of all recovers """
        return {'recovered': int(self.df['Recovered'].sum())}
    
    def get_affected_countries(self) -> Dict[str, List]:
        """ The affected countries """
        countries = self.df['Country'].unique().tolist()
        return {'countries': countries}
