"""
FILE: covid_api_v2_integrator_cases.py
DESCRIPTION: Case Integrators for API v2
AUTHOR: Nuttaphat Arunoprayoch
DATE: 30-March-2021
"""
# Import libraries
from .covid_api_v2_cases_builder import CaseBuilder
    
class CurrentCase:
    "Building a complex representation of the current cases."
    
    @staticmethod
    def construct():
        "Construct and return the data of the current cases"
        return CaseBuilder().get_current()

class USCurrentCase:
    "Building a complex representation of the US current cases."
    
    @staticmethod
    def construct():
        "Construct and return the data of the US current cases"
        return CaseBuilder().get_current_US()

class Country:
    "Building a complex representation of the current cases of a country."
    
    @staticmethod
    def construct(country_name: str):
        "Construct and return the data of the current cases of a country."
        return CaseBuilder().get_country(country_name)

class Confirmed:
    "Building a complex representation of the confirmed cases."
    
    @staticmethod
    def construct():
        "Construct and return the data of the confirmed cases"
        return CaseBuilder().get_confirmed()

class Deaths:
    "Building a complex representation of the deaths cases."
    
    @staticmethod
    def construct():
        "Construct and return the data of the deaths cases"
        return CaseBuilder().get_deaths()

class Recovered:
    "Building a complex representation of the recovered cases."
    
    @staticmethod
    def construct():
        "Construct and return the data of the recovered cases"
        return CaseBuilder().get_recovered()

class Active:
    "Building a complex representation of the active cases."
    
    @staticmethod
    def construct():
        "Construct and return the data of the active cases"
        return CaseBuilder().get_active()

class Total:
    "Building a complex representation of the total cases."
    
    @staticmethod
    def construct():
        "Construct and return the data of the total cases"
        return CaseBuilder().get_total()
