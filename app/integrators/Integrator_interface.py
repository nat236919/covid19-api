from app.integrators.covid_api_v1_integrator import CovidAPIv1
from app.integrators.covid_api_v2_integrator import CovidAPIv2Integrator

class interfaceCovidAPI:

    def __init__(self, v)-> None:
        self.v = 0
        self.iF1 = CovidAPIv1
        self.iF2 = CovidAPIv2Integrator

    def get_deaths(self) -> None:
        if v == 0 :
            CovidAPIv1.get_deaths
        elif: v == 1:
            CovidAPIv2Integrator.get_deaths

    def get_recovered(self) -> None:
        if v == 0 :
            CovidAPIv1.get_recovered
        elif: v == 1:
            CovidAPIv2Integrator.get_recovered

    def get_total(self) -> None:
         if v == 0 :
            CovidAPIv1.get_total
        elif: v == 1:
            CovidAPIv2Integrator.get_total

    def get_time_series(self) -> None:
         if v == 0 :
            CovidAPIv1.get_time_series
         elif v == 1:
            CovidAPIv2Integrator.get_time_series

