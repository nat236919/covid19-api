"""
FILE: country_helper.py
DESCRIPTION: Function for helping 
AUTHOR: Liran Zheku
DATE: 15-March-2021
"""
import pycountry


# Look up a country name from a country code
def helper_lookup_country(country: str) -> str:
    """ Look up a country name from a country code """
    country_name = pycountry.countries.lookup(country).name # Select the first portion of str when , is found
    if ',' in country_name:
        country_name = country_name.split(',')[0]
    elif ' ' in country_name:
        country_name = country_name.split(' ')[-1]
    return country_name
