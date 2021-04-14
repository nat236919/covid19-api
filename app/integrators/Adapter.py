from app.integrators.covid_api_v1_integrator import CovidAPIv1
from app.integrators.covid_api_v2_integrator import CovidAPIv2Integrator

"""Create an adapter class to assign methods in the different integrators into the different routers"""


class Adapter:
    def __init__(self):
        self.v = 0
        self.adapter1 = CovidAPIv1()
        self.adapter2 = CovidAPIv2Integrator()

    def current_status(self, v):
        if self.v == 1:
            self.adapter1.get_current_status()
        if self.v == 2:
            self.adapter2.get_current()

    def total(self, v):
        if self.v == 1:
            self.adapter1.get_total()
        if self.v == 2:
            self.adapter2.get_total()

    def confirmed_cases(self, v):
        if self.v == 1:
            self.adapter1.get_confirmed_cases()
        if self.v == 2:
            self.adapter2.get_confirmed()

    def deaths(self, v):
        if self.v == 1:
            self.adapter1.get_deaths()
        if self.v == 2:
            self.adapter2.get_deaths()

    def recovered(self, v):
        if self.v == 1:
            self.adapter1.get_recovered()
        if self.v == 2:
            self.adapter2.get_recovered()

    def active(self, v):
        if self.v == 2:
            self.adapter2.get_active()

    def affected_countries(self, v):
        if self.v == 1:
            self.adapter1.get_affected_countries()
        if self.v == 2:
            self.adapter2.get_country()

    def time_series(self, v):
        if self.v == 1:
            self.adapter1.get_time_series()
        if self.v == 2:
            self.adapter2.get_time_series()

    def current_us(self, v):
        if self.v == 2:
            self.adapter2.get_current_US()

    def us_time_series (self, v):
        if self.v == 2:
            self.adapter2.get_US_time_series()

    def current_us(self, v):
        if self.v == 2:
            self.adapter2.get_current_US()
