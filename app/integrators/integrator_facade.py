from .covid_api_v1_integrator import CovidAPIv1Integrator
from .covid_api_v2_integrator import CovidAPIv2Integrator

from ..utils.get_data import (DailyReports, DataTimeSeries,
                              get_data_lookup_table)



class Integrator_Facade:

    # version needs to be either 1 or 2
    def __init__(self, version: int, daily_reports: DailyReports = None, time_series: DataTimeSeries = None):
        self.version = version
        if(self.version == 1):
            self.integrator = CovidAPIv1Integrator()
        elif(self.version == 2):
            self.integrator = CovidAPIv2Integrator(daily_reports, time_series)


    def get_integrator(self):
        if(self.version == 1):
            return self.integrator
        elif(self.version == 2):
            return self.integrator


    def get_total(self):
        if(self.version == 1):
            return self.integrator.get_total()
        elif(self.version == 2):
            return self.integrator.get_total()

    def get_confirmed_cases(self):
        if(self.version == 1):
            return self.integrator.get_confirmed_cases()
        elif(self.version == 2):
            return self.integrator.get_confirmed()

    def get_current_status(self, list_required:bool = False):
        if(self.version == 1):
            return self.integrator.get_current_status(list_required)
        elif(self.version == 2):
            return self.integrator.get_current()

    def get_deaths(self):
        if(self.version == 1):
            return self.integrator.get_deaths()
        elif(self.version == 2):
            return self.integrator.get_deaths()

    def get_recovered(self):
        if(self.version == 1):
            return self.integrator.get_recovered()
        elif(self.version == 2):
            return self.integrator.get_recovered()


    def get_time_series(self):
        if(self.version == 1):
            return self.integrator.get_time_series()
        elif(self.version == 2):
            return self.integrator.get_time_series()



        #####################################

    def get_affected_countries(self):
        if(self.version == 1):
            return self.integrator.get_affected_countries()

    def get_country(self, cntry_name: str):
        if(self.version == 2):
            return self.integrator.get_country(cntry_name)

    def get_current(self):
        if(self.version == 2):
            return self.integrator.get_current()

    def get_current_US(self):
        if(self.version == 2):
            return self.integrator.get_current_US()

    def get_active(self):
        if(self.version == 2):
            return self.integrator.get_active()

    def get_US_time_series (self, case:str):
        if(self.version == 2):
            return self.integrator.get_US_time_series(case)

    def get_current_us(self):
        if(self.version == 2):
            return self.integrator.get_current_US()

